#!/usr/bin/env python3
import os
import cgi
from langchain.utilities.dalle_image_generator import DallEAPIWrapper
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# Create an instance of the OpenAI language model
myllm = OpenAI(
    model='text-davinci-003',
    temperature=1,
    openai_api_key=os.environ["OPENAI_API_KEY"]
)

# Create a PromptTemplate
prompt = PromptTemplate(
    input_variables=["image_desc"],
    template="Generate a detailed prompt to generate an image based on the following description: {image_desc}",
)

# Create an LLMChain
chain = LLMChain(llm=myllm, prompt=prompt)

# Create a CGI form instance
form = cgi.FieldStorage()
# Get the image description from the form
prompt_from_front = form.getvalue("image_desc", "")

# Generate image URL using DALL-E through LangChain
image_url = DallEAPIWrapper().run(chain.run(prompt_from_front))

# Print the CGI header
print("Content-Type: text/html\n")

# Print the HTML response
print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Generated Image</title>
</head>
<body>
    <h1>Generated Image</h1>
    <p>Description: {prompt_from_front}</p>
    <img src="{image_url}" alt="Generated Image">
</body>
</html>
""")