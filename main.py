#!/usr/bin/env python3
# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
"""
Run a Flask REST API exposing a YOLOv5s model
"""

import argparse
import io

import torch
from flask import Flask, request, make_response, jsonify
from PIL import Image
import json
#
from utils.file_utils import *
from utils.time_utils import *
from utils.system_utils import *

app = Flask(__name__)
# app.config.from_object(config)

DEV = False


@app.route("/ping", methods=["GET"])
def ping():
    return make_response("pong", 200)

@app.route("/", methods=["GET", "POST"])
def predict():
    if DEV:
        print("files: ", request.files)
        print(request.files.get("image"))
        print("form: ", request.form)
        print("args: ", request.args)
        print("data: ", request.data)
    if request.method == "GET":
        return make_response(jsonify({"response": "get request received"}), 200)

    if request.method == "POST":

        if request.files.get("image"):
            # Method 1
            # with request.files["image"] as f:
            #     im = Image.open(io.BytesIO(f.read()))

            # Method 2
            im_file = request.files["image"]
            im_bytes = im_file.read()
            im = Image.open(io.BytesIO(im_bytes))

            results = model(im, size=640)  # reduce size=320 for faster inference

            # convert results to dict
            cv_results:list = results.pandas().xyxy[0].to_dict(orient="records")
            # out_json = json.dumps(cv_results)
            return make_response(jsonify({"response": cv_results}), 200)
        else:
            return make_response(jsonify({"response": "no 'image' file found"}), 200)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask API exposing YOLOv5 model")
    parser.add_argument("--port", default=1300, type=int, help="port number")
    opt = parser.parse_args()

    # Fix known issue urllib.error.HTTPError 403: rate limit exceeded https://github.com/ultralytics/yolov5/pull/7210
    # torch.hub._validate_not_a_forked_repo = lambda a, b, c: True

    model = torch.hub.load("ultralytics/yolov5", "yolov5s", force_reload=False, skip_validation=True)  # force_reload to recache
    print("DEV: ", DEV)
    app.run(host="0.0.0.0", port=opt.port, debug=True, threaded=False)  # debug=True causes Restarting with stat
