# API_KEY="AIzaSyCD36ou3CJiahfox6PbamLhgxHKVy0banI"

# import pathlib
# import textwrap

# import google.generativeai as genai

# from IPython.display import display
# from IPython.display import Markdown


# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# genai.configure(api_key=API_KEY)

# # for m in genai.list_models():
# #   if 'generateContent' in m.supported_generation_methods:
# #     # print(m.name)

# model = genai.GenerativeModel('gemini-pro')

# prompt="is ther any TraFic Ligt  in the video?"

# response = model.generate_content(f"What is the object specified in the given prompt :{prompt}  the list of objects are ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'] ")

# print(response.text)
# to_markdown(response.text)


import textwrap
import google.generativeai as genai
from IPython.display import Markdown

class GenerativeModelWrapper:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_response(self, prompt):
        response = self.model.generate_content(f"What is the object specified in the given prompt :{prompt}  the list of objects are ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'] ")
        return response.text

    @staticmethod
    def to_markdown(text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Usage:
API_KEY = "AIzaSyCD36ou3CJiahfox6PbamLhgxHKVy0banI"
model_wrapper = GenerativeModelWrapper(API_KEY)
prompt = "is ther any TraFic Ligt  in the video?"
response_text = model_wrapper.generate_response(prompt)
print(response_text)
