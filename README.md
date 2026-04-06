A collection of Python scripts demonstrating direct LLM API integration 
using OpenAI — no frameworks, no abstractions. Built as part of an AI 
engineering learning path.
1. text summarizer -> Text summarizer uses openAi api for summarizing the text in 3 bullet points.
2. text classifier -> Text classifier uses openAi for identifying the tone of the text across..complaints, compliments, feedback, etc.
3. text summarizer with fast api -> This code is just similar to script1 one only difference is I'm using FastApi FastAPI to expose the summarizer as an HTTP endpoint over the internet

4. ## Scripts

### 1. Text Summarizer
Summarizes long text into 3 bullet points using OpenAI.
Input: long article text  
Output: `• Point 1 \n• Point 2 \n• Point 3`

### 2. Intent Classifier  
Classifies user messages into: question, complaint, request, compliment, other.
Input: `"My order arrived damaged"`  
Output: `{"intent": "complaint", "confidence": "high"}`

### 3. FastAPI Summarizer
Exposes the summarizer as a REST endpoint.
`POST /summarize` → `{"text": "..."}` → `{"summary": "..."}`

## Setup
pip install -r requirements.txt  
Add OPENAI_API_KEY to .env  
uvicorn api:app --reload
