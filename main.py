import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")#Read the API key from .env so we don't hard-code secrets
    if api_key == None:
        raise RuntimeError("GEMINI_API_KEY enviroment variable not set")
    
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    generate_content(client, messages, args.verbose, args.user_prompt)


def generate_content(client, messages, verbose, user_prompt):   
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents= messages
    )
    if response.usage_metadata == None:
        raise RuntimeError("Gemini API response appears to be malformed")
    
    if verbose:
        print("User prompt:", user_prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)     
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
