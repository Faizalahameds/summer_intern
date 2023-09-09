#/usr/bin/python3
import json
import openai

# Set the appropriate headers for a CGI script
print("Content-Type: text/html")
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print()

# Get the user's message from the request
form = cgi.FieldStorage()
user_message = form.getvalue('message')

# Set your OpenAI API key here
openai.api_key = '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'

# Generate response using OpenAI GPT-3
response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=user_message,
    max_tokens=150,
    temperature=0.7,  # Adjust temperature for desired creativity
    n=1,
    stop=None
)

# Extract and print the generated response
generated_response = response.choices[0].text.strip()
print(f"<h2>Generated Response:</h2><p>{generated_response}</p>")