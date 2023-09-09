#!/usr/bin/python3

import cgi
import os
import boto3

# AWS credentials (replace with your own)
aws_access_key_id = 'AKIARZSCORSQDPP3IEOG'
aws_secret_access_key = '1E2an8Rbr9m40+AzYtmQKTy5cv52gHEj1H3q94Eh'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# S3 bucket and object details
bucket_name = 'trans12'

print("Content-type: text/html\n\n")

def save_uploaded_file(file_item):
    # Construct S3 object key using the original filename
    object_key = os.path.basename(file_item.filename)

    # Upload the file to S3
    s3.upload_fileobj(file_item.file, bucket_name, object_key)

    return object_key

def main():
    form = cgi.FieldStorage()
    if 'file' in form:
        uploaded_file = form['file']
        if uploaded_file.filename:
            saved_object_key = save_uploaded_file(uploaded_file)
            print(f"<p>File '{saved_object_key}' uploaded to S3 bucket '{bucket_name}'</p>")
        else:
            print("<p>No file selected or empty file.</p>")
    else:
        print("<p>No file uploaded.</p>")

if __name__ == "__main__":
    main()