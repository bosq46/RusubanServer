#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response
import os
import werkzeug
from datetime import datetime

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# limit upload file size : 10MB
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
# ex) set UPLOAD_DIR_PATH=C:/tmp/flaskUploadDir
# UPLOAD_DIR = os.getenv("UPLOAD_DIR_PATH")
UPLOAD_DIR = "./uploads"


@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        make_response(jsonify({'result': 'audio is required.'}))

    file = request.files['audio']
    fileName = file.filename
    if '' == fileName:
        make_response(jsonify({'result':'filename must not empty.'}))

    saveFileName = datetime.now().strftime("%Y%m%d%H%M%S_") \
        + werkzeug.utils.secure_filename(fileName)
    file.save(os.path.join(UPLOAD_DIR, saveFileName))
    return make_response(jsonify({'result':'upload OK.'}))


@app.errorhandler(werkzeug.exceptions.RequestEntityTooLarge)
def handle_over_max_file_size(error):
    print("werkzeug.exceptions.RequestEntityTooLarge")
    return 'result : file size is overed.'


if __name__ == "__main__":

    app.run(debug=True)

