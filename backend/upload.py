#!/usr/bin/python3
import cgi
import os
import time
import cv2
import time
import subprocess


from cvzone.HandTrackingModule import HandDetector
upload_dir = "myupload/"

print("Content-Type: text/plain")
print()

try:
    form = cgi.FieldStorage()
    image_file = form['image']

    if image_file.filename:
        timestamp = int(time.time())
#        filename = f"image_{timestamp}.png"
        filename = "myimage.png"

        filepath = os.path.join(upload_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(image_file.file.read())
        print("<p>Live Streaming Started ..</p>")
    else:
        print("No image file received")
except Exception as e:
    print("An error occurred:", str(e))

def launch_centos_container():
    try:

        subprocess.run(["sudo", "docker", "run", "-dit", "centos"])
        print("<p>CentOS container launched successfully!</p>")
    except subprocess.CalledProcessError as e:
      print(f"<p>An error occurred: {e}</p>")

detector = HandDetector(maxHands=1,
                        detectionCon=0.8)

img = cv2.imread("myupload/myimage.png")

hand = detector.findHands(img , draw=False)
if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            print(fingerup)
            if fingerup == [0, 1, 0, 0, 0]:
                print("index finger ..")
                launch_centos_container()

            elif fingerup == [0, 1, 1, 0, 0]:
                print("index and middle finger ..")
                launch_centos_container()
                launch_centos_container()
            else:
                print("i work with index or middle finger ..")

else:
        print("no hand detected")