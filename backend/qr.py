#!/usr/bin/python3

import cgi
import qrcode
from PIL import Image
import base64
import io

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
data = form.getvalue("data")

if data:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Convert PIL image to bytes
    img_byte_array = io.BytesIO()
    img.save(img_byte_array, format="PNG")
    img_bytes = img_byte_array.getvalue()
 # Encode image bytes to base64
    img_base64 = base64.b64encode(img_bytes).decode("utf-8")

    print("<h2>QR Code generated successfully:</h2>")
    print(f'<img src="data:image/png;base64,{img_base64}" alt="QR Code">')
else:
    print("<h2>No data provided.</h2>")
