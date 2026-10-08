"""
import os
from dotenv import load_dotenv
from google.genai import Client

# Load the keys from the .env file
load_dotenv()

# Configure the Gemini client with your key
client=Client(api_key=os.getenv("GEMINI_API_KEY"))


# Select the fast, free model

def analyze_article(text):
    prompt="please summarize this new headline in one short,engaging sentence: "+text
    response= client.models.generate_content(model="gemini-3.8-flash",contents=prompt)
    return response.text

"""

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_article(text: str):
    prompt = "Please summarize this news headline in one short, engaging sentence: " + text
    
    # Use the Chat session exactly like the error requested, keeping it incredibly simple
    chat = client.chats.create(model="gemini-3.8-flash")
    response = chat.send_message(prompt)
    
    return response.text

