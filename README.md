# Language-Detector
# AI Language Detector

A complete web application for detecting languages from text using AI-powered language detection.

## Features

- **Real-time Language Detection**: Detects languages from text input with confidence scores
- **Multi-language Support**: Supports 55+ languages including English, Spanish, French, German, Chinese, Japanese, Arabic, and more
- **Responsive Web Interface**: Modern, mobile-friendly UI with smooth animations
- **Confidence Scoring**: Shows probability distribution for all detected languages
- **Sample Text Testing**: Quick test buttons for different languages
- **RESTful API**: Clean API endpoints for integration with other applications

## Project Structure

```
language-detector/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend HTML/CSS/JS
└── README.md             # This file
```

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Step 1: Clone/Download the Code
Save the provided files in a directory structure as shown above.

### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Create Templates Directory
```bash
mkdir templates
```
Make sure the `index.html` file is placed in the `templates/` directory.

### Step 5: Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5000`

## API Endpoints

### POST /api/detect
Detects language from input text.

**Request Body:**
```json
{
    "text": "Hello, how are you today?"
}
```

**Response:**
```json
{
    "success": true,
    "detected_language": {
        "code": "en",
        "name": "English"
    },
    "all_detections": [
        {
            "language_code": "en",
            "language_name": "English",
            "confidence": 0.9999
        }
    ],
    "text_length": 26
}
```

### GET /api/supported-languages
Returns list of all supported languages.

### GET /api/health
Health check endpoint.

## Supported Languages

The application supports 55+ languages including:
- English, Spanish, French, German, Italian
- Chinese (Simplified & Traditional), Japanese, Korean
- Arabic, Hindi, Russian, Portuguese
- And many more...

## Usage Examples

### Web Interface
1. Open `http://localhost:5000` in your browser
2. Enter text in the textarea
3. Click "Detect Language" or press Ctrl+Enter
4. View results with confidence scores

### API Usage with curl
```bash
# Detect language
curl -X POST http://localhost:5000/api/detect \
  -H "Content-Type: application/json" \
  -d '{"text": "Bonjour, comment allez-vous?"}'

# Get supported languages
curl http://localhost:5000/api/supported-languages
```

### API Usage with Python
```python
import requests

# Detect language
response = requests.post('http://localhost:5000/api/detect', 
                        json={'text': 'Hola, ¿cómo estás?'})
result = response.json()
print(f"Detected: {result['detected_language']['name']}")
```

## Features in Detail

### Language Detection Engine
- Uses the `langdetect` library (port of Google's language-detection library)
- Provides confidence scores for multiple possible languages
- Handles short text detection with appropriate error handling

### Web Interface
- Modern, responsive design with gradient backgrounds
- Real-time feedback with loading states
- Error handling for various edge cases
- Sample text buttons for quick testing
- Mobile-optimized layout

### API Design
- RESTful endpoints with JSON responses
- CORS enabled for cross-origin requests
- Comprehensive error handling
- Input validation and sanitization

## Error Handling

The application handles various error cases:
- Empty or too short text input
- Network connectivity issues
- Invalid JSON requests
- Language detection failures

## Deployment

### Local Development
The application runs on `http://localhost:5000` by default.

### Production Deployment
For production, use a WSGI server like Gunicorn:
```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

### Docker Deployment
You can also containerize the application:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

## Customization

### Adding New Languages
To add support for new languages, update the `LANGUAGE_NAMES` dictionary in `app.py`.

### Styling Changes
Modify the CSS in `templates/index.html` to customize the appearance.

### API Extensions
Add new endpoints in `app.py` for additional functionality.

## Troubleshooting

### Common Issues:
1. **Module not found**: Ensure virtual environment is activated and dependencies are installed
2. **Port already in use**: Change port in `app.py` or stop other services using port 5000
3. **Template not found**: Ensure `index.html` is in the `templates/` directory
4. **Detection fails**: Check input text length (minimum 3 characters required)

### Debug Mode
The application runs in debug mode by default. For production, set `debug=False` in `app.py`.

## Contributing

Feel free to contribute by:
- Adding support for more languages
- Improving the UI/UX
- Adding new API features
- Optimizing performance
- Writing tests

## License

This project is open source and available under the MIT License.
