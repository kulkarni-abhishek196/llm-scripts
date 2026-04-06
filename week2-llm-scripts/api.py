from fastapi import FastAPI
from pydantic import BaseModel
from script1_summarizer import TextSummarizer

import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

summarizer = TextSummarizer(
    url="https://api.openai.com/v1/chat/completions",
    model='gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)


class SummarizeRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize(request: SummarizeRequest):
    result = summarizer.summarize(request.text)
    return {"summary": result}