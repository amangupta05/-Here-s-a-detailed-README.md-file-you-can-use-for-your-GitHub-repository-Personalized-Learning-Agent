import openai
from config.config import config

openai.api_key = config.GPT4_API_KEY

def query_gpt4(prompt, temperature=0.7):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"