#!/usr/bin/python3
import cgi
import boto3

print("Content-Type: text/html")
print()

# Replace with your AWS access key ID and secret access key
aws_access_key_id = 'AKIARZSCORSQDPP3IEOG'
aws_secret_access_key = '1E2an8Rbr9m40+AzYtmQKTy5cv52gHEj1H3q94Eh'


def detect_labels(image_data):
    client = boto3.client('rekognition', region_name='ap-south-1',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)
    response = client.detect_labels(Image={'Bytes': image_data}, MaxLabels=8)
    labels = response["Labels"]
    result_text = "<h2>Label Detection Results:</h2><ul>"
    for label in labels:
        result_text += f"<li>Label: {label['Name']}, Confidence: {label['Confidence']:.2f}%</li>"
    result_text += "</ul>"
    return result_text

form = cgi.FieldStorage()

# Check if the form was submitted
if "image" in form:
    image_file = form["image"]
    if image_file.filename:
        else:
        result_text = "<h2>No image uploaded.</h2>"
else:
    result_text = ""

# Display HTML form and results
with open("/var/www/html/image_label_detection_form.html", "r") as html_file:
    html_content = html_file.read()
    print(html_content.replace("{{result}}", result_text))