API_KEY="AIzaSyCD36ou3CJiahfox6PbamLhgxHKVy0banI"

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=API_KEY)

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     # print(m.name)

model = genai.GenerativeModel('gemini-pro')

prompt="is ther any riot happen here?"

response = model.generate_content(f"classify the tex  ")

print(response.text)
to_markdown(response.text)