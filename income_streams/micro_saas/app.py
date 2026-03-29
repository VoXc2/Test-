"""Micro-SaaS AI Tools Web App - Income Stream #3.

A FastAPI web app hosting AI-powered tools behind a clean UI.
Monetize with ads, freemium model, or API access.

Usage:
    uvicorn income_streams.micro_saas.app:app --reload
    # Then open http://localhost:8000
"""

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .tools.text_summarizer import TextSummarizer
from .tools.email_writer import EmailWriter
from .tools.grammar_checker import GrammarChecker

app = FastAPI(title="AI Tools Hub", description="أدوات ذكاء اصطناعي مجانية")

# Initialize tools
summarizer = TextSummarizer()
email_writer = EmailWriter()
grammar_checker = GrammarChecker()

TEMPLATE_DIR = Path(__file__).parent / "templates"


# --- Models ---
class SummarizeRequest(BaseModel):
    text: str
    length: str = "medium"
    language: str = "auto"


class EmailRequest(BaseModel):
    purpose: str
    recipient: str = ""
    tone: str = "professional"
    language: str = "ar"
    context: str = ""


class GrammarRequest(BaseModel):
    text: str
    language: str = "auto"


# --- Routes ---
@app.get("/", response_class=HTMLResponse)
async def home():
    html_path = TEMPLATE_DIR / "index.html"
    return HTMLResponse(content=html_path.read_text(encoding="utf-8"))


@app.post("/api/summarize")
async def api_summarize(req: SummarizeRequest):
    try:
        result = summarizer.summarize(req.text, length=req.length, language=req.language)
        return {"result": result}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.post("/api/write-email")
async def api_write_email(req: EmailRequest):
    try:
        result = email_writer.write(
            purpose=req.purpose,
            recipient=req.recipient,
            tone=req.tone,
            language=req.language,
            context=req.context,
        )
        return {"result": result}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.post("/api/check-grammar")
async def api_check_grammar(req: GrammarRequest):
    try:
        result = grammar_checker.check(req.text, language=req.language)
        return {"result": result}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/api/health")
async def health():
    return {"status": "ok", "tools": ["summarizer", "email_writer", "grammar_checker"]}
