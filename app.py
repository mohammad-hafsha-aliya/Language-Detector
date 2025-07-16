from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import langdetect
from langdetect import detect, detect_langs
from langdetect.lang_detect_exception import LangDetectException
import logging

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Language code to name mapping
LANGUAGE_NAMES = {
    'af': 'Afrikaans', 'ar': 'Arabic', 'bg': 'Bulgarian', 'bn': 'Bengali',
    'ca': 'Catalan', 'cs': 'Czech', 'cy': 'Welsh', 'da': 'Danish',
    'de': 'German', 'el': 'Greek', 'en': 'English', 'es': 'Spanish',
    'et': 'Estonian', 'fa': 'Persian', 'fi': 'Finnish', 'fr': 'French',
    'gu': 'Gujarati', 'he': 'Hebrew', 'hi': 'Hindi', 'hr': 'Croatian',
    'hu': 'Hungarian', 'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese',
    'kn': 'Kannada', 'ko': 'Korean', 'lt': 'Lithuanian', 'lv': 'Latvian',
    'mk': 'Macedonian', 'ml': 'Malayalam', 'mr': 'Marathi', 'ne': 'Nepali',
    'nl': 'Dutch', 'no': 'Norwegian', 'pa': 'Punjabi', 'pl': 'Polish',
    'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian', 'sk': 'Slovak',
    'sl': 'Slovenian', 'so': 'Somali', 'sq': 'Albanian', 'sv': 'Swedish',
    'sw': 'Swahili', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai',
    'tl': 'Filipino', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu',
    'vi': 'Vietnamese', 'zh-cn': 'Chinese (Simplified)', 'zh-tw': 'Chinese (Traditional)'
}

def get_language_name(lang_code):
    """Convert language code to full language name"""
    return LANGUAGE_NAMES.get(lang_code, lang_code.upper())

@app.route('/')
def index():
    """Serve the frontend HTML page"""
    return render_template('index.html')

@app.route('/api/detect', methods=['POST'])
def detect_language():
    """API endpoint to detect language from text"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400
        
        text = data['text'].strip()
        
        if not text:
            return jsonify({'error': 'Empty text provided'}), 400
        
        if len(text) < 3:
            return jsonify({'error': 'Text too short for reliable detection'}), 400
        
        # Detect the most likely language
        detected_lang = detect(text)
        
        # Get probability distribution for all detected languages
        lang_probs = detect_langs(text)
        
        # Format the results
        results = []
        for lang_prob in lang_probs:
            results.append({
                'language_code': lang_prob.lang,
                'language_name': get_language_name(lang_prob.lang),
                'confidence': round(lang_prob.prob, 4)
            })
        
        response = {
            'success': True,
            'detected_language': {
                'code': detected_lang,
                'name': get_language_name(detected_lang)
            },
            'all_detections': results,
            'text_length': len(text)
        }
        
        logger.info(f"Detected language: {detected_lang} for text of length {len(text)}")
        return jsonify(response)
        
    except LangDetectException as e:
        logger.error(f"Language detection error: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Could not detect language. Please try with more text or different content.'
        }), 400
        
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'An unexpected error occurred'
        }), 500

@app.route('/api/supported-languages', methods=['GET'])
def get_supported_languages():
    """Get list of supported languages"""
    return jsonify({
        'success': True,
        'languages': LANGUAGE_NAMES
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Language Detector API'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)