# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
"""
Perform test request
"""
import os.path
import pprint

import requests

DETECTION_URL = "http://localhost:1300/"
IMAGE = os.path.join(os.getcwd(), "data", "ch01_20220718133220_intrusionCap.jpg")

# Read image
with open(IMAGE, "rb") as f:
    image_data = f.read()

response = requests.post(DETECTION_URL, files={"image": image_data}).json()

pprint.pprint(response)
