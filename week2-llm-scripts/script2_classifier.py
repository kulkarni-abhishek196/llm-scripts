import os
import json
from dotenv import load_dotenv
import requests

load_dotenv()
class TextClassifier:

    def __init__(self, url:str, model:str, api_key:str):
        self.url = url
        self.model = model
        self.api_key = api_key

    def classifier(self, message:str)->dict:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model":self.model,
            "temperature": 0.1,
            "response_format": {"type":"json_object"},
            "messages":[
                {"role":"system", "content":"you are a tone classfier assistant. you take the user message and classifies into one of 5 categories : question, request, complaint, compliment, other. Also respond in the json format as : {\"intent\": \"complaint\", \"confidence\": \"high\"}"},
                {"role":"user", "content": message}
            ]
        }
        response = requests.post(url=self.url, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            generated_output = result['choices'][0]['message']['content']
        try:
            return json.loads(generated_output)
        except json.JSONDecodeError:
            return {"error": "invalid JSON", "raw": generated_output}


api_key = os.getenv("OPENAI_API_KEY")
model = "gpt-4o-mini"
url = "https://api.openai.com/v1/chat/completions"

# cl1 = TextClassifier(url=url, model=model, api_key=api_key)
# ans = cl1.classifier("I received my order today, but the glass vase inside was shattered. The packaging was completely inadequate.")

# print(ans)