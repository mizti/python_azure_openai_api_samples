from azure.identity import AzureCliCredential
import os
from openai import AzureOpenAI
from azure.identity import get_bearer_token_provider

model_deploy_name=os.environ["MODEL_DEPLOY_NAME"]
aoai_endpoint=os.environ["AOAI_ENDPOINT"]
api_version=os.environ["API_VERSION"]
# Needed Role: Cognitive Services OpenAI User 

# CLI Credential
token_provider = get_bearer_token_provider(AzureCliCredential(), "https://cognitiveservices.azure.com/.default")

client = AzureOpenAI(
    azure_endpoint=aoai_endpoint, 
    api_version=api_version,
    azure_ad_token_provider=token_provider)

messages = [{"role":"system","content":"あなたは私のAIアシスタントです。できるだけ簡潔に回答してください。"},{"role":"user","content":"同窓会の紹介状の文例。"},{"role":"assistant","content":"尊敬するXXさんへ\n\nお元気でお過ごしでしょうか。私たちは、XX年に同じ学校で学んだ仲間たちで、このたび同窓会を開催することになりました。\n\n日時：XX年XX月XX日（土）XX時から\n場所：XXホテル 2階 パーティールーム\n\n当日は、"}]

response = client.chat.completions.create(model=model_deploy_name,
    messages = messages,
    temperature=0.5,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)

print(response.to_dict())