# AI Assistant

A small FastAPI app that serves a web page and forwards chat messages to the Google Gemini Generative AI API using the `google.genai` client.

## Project structure

- `main.py` - FastAPI application entry point
- `templates/index.html` - browser UI for sending messages and showing responses
- `myenv/` - local Python virtual environment

## Setup

1. Activate the virtual environment:

   ```powershell
   .\myenv\Scripts\Activate.ps1
   ```

2. Install dependencies if needed:

   ```powershell
   pip install -r requirements.txt
   ```

   If `requirements.txt` is not present, install:

   ```powershell
   pip install fastapi uvicorn python-dotenv google-genai
   ```

3. Create a `.env` file in the project root with your Gemini API key:

   ```text
   GEMINI_API_KEY=your_api_key_here
   ```

## Run the app

Start the server with:

```powershell
uvicorn main:app --reload
```

Then open `http://127.0.0.1:8000` in your browser.

## Notes

- The app uses the Gemini model `gemini-2.0-flash`.
- If the API key does not have quota, the page may show a `429 RESOURCE_EXHAUSTED` message.
- The UI is a simple single-page form that sends a JSON POST to `/chat` and displays the response.

## Troubleshooting

- If you see an error loading the page, check that `templates/index.html` exists and is not empty.
- If `/chat` returns a quota error, verify your Gemini billing/plan and API key.
