#!/usr/bin/env python
# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
"""
Perform test request
"""
import os.path
import pprint

import requests

# DETECTION_URL = "http://localhost:1300/"
DETECTION_URL = "http://172.17.0.2:1300/"
IMAGE = os.path.join(os.getcwd(), "data", "zidane.jpg")

# Read image
with open(IMAGE, "rb") as f:
    image_data = f.read()

response = requests.post(DETECTION_URL, files={"image": image_data}).json()

pprint.pprint(response)
