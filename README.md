# AI Assistant

A lightweight AI assistant built using FastAPI and Google Gemini API.  
This project provides a simple web-based chat interface where users can send messages and receive AI-generated responses in real time.

---

# Features

- FastAPI backend
- Google Gemini AI integration
- Simple browser-based chat UI
- Environment variable support using `.env`
- Lightweight and beginner-friendly architecture

---

# Project Structure

```text
AI-Assistant/
│
├── main.py                 # FastAPI application
├── templates/
│   └── index.html          # Frontend chat interface
├── .env                    # API keys (not uploaded to GitHub)
├── .gitignore
├── requirements.txt
└── myenv/                  # Virtual environment
```

---

# Tech Stack

- Python
- FastAPI
- Google Gemini API
- HTML / JavaScript
- Jinja2 Templates

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd AI-Assistant
```

---

## 2. Create and Activate Virtual Environment

### Windows PowerShell

```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

If `requirements.txt` is unavailable:

```powershell
pip install fastapi uvicorn python-dotenv google-genai jinja2
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

---

# Running the Application

Start the FastAPI development server:

```powershell
uvicorn main:app --reload
```

Open your browser and visit:

```text
http://127.0.0.1:8000
```

---

# API Endpoint

## POST `/chat`

Sends a user message to the Gemini model and returns the AI response.

### Example Request

```json
{
  "message": "Hello AI"
}
```

### Example Response

```json
{
  "reply": "Hello! How can I help you today?"
}
```

---

# Model Used

This project currently uses:

```text
gemini-2.0-flash
```

---

# Security Notes

- Never upload your `.env` file to GitHub.
- Keep your API keys private.
- `.gitignore` should include:

```text
.env
myenv/
__pycache__/
```

---

# Troubleshooting

## Template Errors

Ensure the file exists:

```text
templates/index.html
```

---

## API Errors / Quota Errors

If you receive:

```text
429 RESOURCE_EXHAUSTED
```

Then:
- Verify your Gemini API quota
- Check API key validity
- Ensure billing/quota limits are available

---

# Future Improvements

- Chat history
- Streaming responses
- Better UI/UX
- Authentication
- Database integration
- Voice input/output
- Multi-model support

---

# License

This project is open-source and free to use for learning purposes.
