#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
from openai import util
import json
openai.api_type = "azure"
openai.api_base = "https://youropenaiapi.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = os.environ["OPENAI_API_KEY"]

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
