# load_env_key.py
from dotenv import load_dotenv
import os

def main():
    # Load environment variables from .env file in the current directory
    load_dotenv()

    # Retrieve the NEWS_API_KEY variable
    news_api_key = os.getenv("API_key")

    # Check if the key exists and print the result
    if news_api_key:
        print("NEWS_API_KEY found ")
    else:
        print("NEWS_API_KEY not found")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")