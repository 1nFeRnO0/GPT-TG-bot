import os
from dotenv import load_dotenv

import httpx
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.getenv('AI_TOKEN')
                     )

async def gpt4(question):
    response = await client.chat.completions.create(
        messages=[{'role': 'user',
                   'content': str(question)}],
                   model='gpt-3.5-turbo-0125'
    )
    return response

# if __name__ == "__main__":
#     response = gpt4('Какова высота эвереста')
#     response_p = response.choices[0].message.content
#     print(response_p)