
import os
from openai import OpenAI

try:
    client = OpenAI(api_key=os.environ.get('openai'))
    if not client.api_key:
        raise ValueError("OpenAI API key not found in environment variables")

    prompt = "Who is the most handsome bald man?"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    print(response.choices[0].message.content)

except Exception as e:
    print(f"Error: {e}")
