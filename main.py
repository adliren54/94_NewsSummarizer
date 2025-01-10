import os, requests, json
import google.generativeai as genai

newsKey = os.environ['newsapi']
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")


country = "us"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}"

result = requests.get(url)
data = result.json()
#print(json.dumps(data, indent=2))

counter = 0
for article in data['articles']:
    counter += 1
    if counter > 5:
        break
    prompt = f"Summarize {article['url']} in one sentence."
    chat = model.start_chat()
    response = chat.send_message(prompt)
    print(response.text)