import requests
import os
from dotenv import load_dotenv


class TextSummarizer:
    
    def __init__(self, url:str, model:str, api_key:str, temperature:float = 0.3)->None:
        self.url = url
        self.model = model
        self.api_key = api_key
        self.temperature = temperature

    def summarize(self, text:str):

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model": f"{self.model}",
            "temperature": self.temperature,    
            "messages": [
                {
                    "role": "system",
                    "content": "You're a helpful assistant. You'd be provided with a long text, you have to summarize the whole text in 3 bullet points"
                },
                {
                    "role": "user",
                    "content": f"{text}"
                }
            ]
        }
        response = requests.post(self.url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"Error {response.status_code}: {response.text}"
        

    def __repr__(self)->str:
        return f"Model : {self.model} with URL : {self.url}"


api_key = os.getenv("OPEN_AI_API_KEY")
model = 'gpt-4o-mini'
url = "https://api.openai.com/v1/chat/completions"

c1 = TextSummarizer(url=url, model=model, api_key=api_key)

# text = "The James Webb Space Telescope (JWST), launched in December 2021, represents a massive leap in astronomical technology. Operating primarily in the infrared spectrum, it allows scientists to peer through cosmic dust clouds that obscure the view of older telescopes like Hubble. Its primary mirror, composed of 18 hexagonal segments coated in gold, spans 6.5 meters. Currently stationed at the second Lagrange point (L2), nearly 1.5 million kilometers from Earth, JWST is designed to study the formation of the first galaxies and the atmospheres of potentially habitable exoplanets."
# print(c1.summarize(text))