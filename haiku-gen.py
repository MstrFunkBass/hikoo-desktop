import os
import openai

open_ai_api_key = os.environ['OPENAI_API_KEY']

def return_haiku():
    
    openai.api_key = open_ai_api_key

    completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello Chat, please generate me a humorous original haiku in lowercase."}
    ]
    )

    haiku = completion.choices[0].message.content.split('\n')

    line_1, line_2, line_3 = haiku[0], haiku[1], haiku[2]

    return [line_1, line_2, line_3]
    # return ["this is my haiku,", "it is the best I have done,", "thanks for listening"] ## -- For Testing