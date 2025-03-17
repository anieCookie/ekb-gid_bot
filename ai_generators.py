import asyncio
from mistralai import Mistral
from config import API_AI_TOKEN
import os

async def generate(messages):
    s = Mistral(
        api_key=API_AI_TOKEN,
    )
    res = await s.chat.complete_async(model="mistral-large-latest", messages=messages)
    if res is not None:
        return res

