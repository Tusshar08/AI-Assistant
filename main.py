from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from dotenv import load_dotenv
import google.genai as genai
from google.genai.errors import ClientError
import os

# Load environment variables from .env
load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Create a Gemini client using the API key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"request": request})

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=req.message,
        )
        return {"reply": response.text}
    except ClientError as exc:
        status_code = getattr(exc, "code", 500)
        try:
            status_code = int(status_code)
        except (TypeError, ValueError):
            status_code = 500
        message = getattr(exc, "message", str(exc))
        if isinstance(message, str):
            lines = [line.strip() for line in message.splitlines() if line.strip()]
            if lines:
                main = lines[0]
                retry = next((line for line in lines if line.lower().startswith("please retry")), None)
                if retry:
                    main = f"{main} ({retry})"
                message = main
        return JSONResponse(
            status_code=status_code,
            content={"error": message},
        )
    except Exception as exc:
        return JSONResponse(
            status_code=500,
            content={"error": str(exc)},
        )