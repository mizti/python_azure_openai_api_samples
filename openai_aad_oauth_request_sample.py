#Note: The openai-python library support for Azure OpenAI is in preview.
from azure.identity import DefaultAzureCredential
from azure.identity import ClientSecretCredential
from azure.identity import AzureCliCredential
import os
import openai
from openai import util
import json

# Needed Role: Cognitive Services OpenAI User 

# Default Credential
#default_credential = DefaultAzureCredential()
#token = default_credential.get_token("https://cognitiveservices.azure.com/.default")

# CLIENT_ID/SECRET Credential
#client_id = os.environ["AZURE_CLIENT_ID"]
#client_secret = os.environ["AZURE_CLIENT_SECRET"]
#tenant_id = os.environ["AZURE_TENANT_ID"]
#credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
#token = credential.get_token("https://cognitiveservices.azure.com/.default")

# CLI Credential
credential = AzureCliCredential()
token = credential.get_token("https://cognitiveservices.azure.com/.default")

openai.api_type = "azure_ad"
openai.api_base = "https://youropenaiapi.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = token.token

response = openai.ChatCompletion.create(
  engine="gpt35",
  messages = [{"role":"system","content":"あなたは私のAIアシスタントです。できるだけ簡潔に回答してください。"},{"role":"user","content":"同窓会の紹介状の文例。"},{"role":"assistant","content":"尊敬するXXさんへ\n\nお元気でお過ごしでしょうか。私たちは、XX年に同じ学校で学んだ仲間たちで、このたび同窓会を開催することになりました。\n\n日時：XX年XX月XX日（土）XX時から\n場所：XXホテル 2階 パーティールーム\n\n当日は、"}],
  temperature=0.5,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

response_txt = util.convert_to_dict(response)
print(response_txt)
