import os
import openai

open_ai_api_key = os.environ['OPENAI_API_KEY']

def return_haiku(test:bool=False)->list:
    """
    Queries chatgpt 3.5 via openai api, and returns a Haiku.
    The Haiku is split into 3 items in a list.
    Example output: ["this is my haiku,", "it is the best I have done,", "thanks for listening"]
    """
    if not test:
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
    else:
        return ['sitting on my couch', 'eating way too many snacks', 'pants no longer fit'] ## -- For Testing

def generate_image(haiku_prompt:str, test:bool=False):

    if not test:
        image_prompt = f'generate a painterly image with a slight green hue, based on the following haiku: {haiku_prompt}'

        openai.api_key = open_ai_api_key

        response = openai.images.generate(
            prompt=image_prompt,
            n=1,
            size="1024x1024",
        )

        return response.data[0].url
    else:
        return 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-QN3KkmyxJWqyPbyp89AdH1VZ/user-OdIZqaOu4VsWPc9OG73dZAIB/img-u54sGh1Gpu9Zh6VYs4LUnr1i.png?st=2025-01-08T14%3A11%3A29Z&se=2025-01-08T16%3A11%3A29Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-01-07T23%3A50%3A46Z&ske=2025-01-08T23%3A50%3A46Z&sks=b&skv=2024-08-04&sig=1RxwQVM/IZPmQrPEjI81nHxzu6oWFOUhF/rD%2BztvS%2BM%3D'