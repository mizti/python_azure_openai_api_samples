import os
import openai
from openai import AsyncAzureOpenAI
from typing import AsyncIterator
import asyncio
from azure.identity import AzureCliCredential
from azure.identity import get_bearer_token_provider

model_deploy_name=os.environ["MODEL_DEPLOY_NAME"]
aoai_endpoint=os.environ["AOAI_ENDPOINT"]
api_version=os.environ["API_VERSION"]
token_provider = get_bearer_token_provider(AzureCliCredential(), "https://cognitiveservices.azure.com/.default")

async def stream_processor(response: AsyncIterator) -> AsyncIterator[str]:
    async for chunk in response:
        if len(chunk.choices) > 0:
            delta = chunk.choices[0].delta
            if delta.content:
                await asyncio.sleep(0.01)
                yield delta.content

async def fetch_gpt_response(messages: list, model: str, client: AsyncAzureOpenAI):
    response = await client.chat.completions.create(model=model_deploy_name,
        messages = messages,
        temperature=0.5,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=True)
    async for content in stream_processor(response):
        yield content


async def main():
    messages = [{"role":"system","content":"あなたは私の文章作成AIアシスタントです。与えられた文の書き出しに対して、できるだけ丁寧で長い文案してください。"},{"role":"user","content":"同窓会の紹介状の文例。"},{"role":"assistant","content":"尊敬するXXさんへ\n\nお元気でお過ごしでしょうか。私たちは、XX年に同じ学校で学んだ仲間たちで、このたび同窓会を開催することになりました。\n\n日時：XX年XX月XX日（土）XX時から\n場所：XXホテル 2階 パーティールーム\n\n当日は、"}]
    model = model_deploy_name
    client = AsyncAzureOpenAI(
        azure_endpoint=aoai_endpoint, 
        api_version=api_version, 
        azure_ad_token_provider=token_provider)

    async for content in fetch_gpt_response(messages, model, client):
        print(content, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
