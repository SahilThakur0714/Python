from openai import OpenAI

client = OpenAI(
    # api_key="",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "What is Coding"}
    ]
)

print(completion.choices[0].message)
