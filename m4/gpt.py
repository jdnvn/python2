from openai import OpenAI

API_KEY="your api key"

client = OpenAI(
    api_key=API_KEY
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What are mind goblins?",
        }
    ],
    model="gpt-4o"
)
print(chat_completion.choices[0].message.content)
