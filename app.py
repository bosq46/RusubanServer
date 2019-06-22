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

# # curl -X POST -H 'Content-Type:application/json' -d '{"user_id": "1", "text": "hoge"}' localhost:5000/posts/create
# @app.route('/posts/create', methods=['POST'])
# def post_create():
#     # 新規投稿作成
#     try:
#         post_json = request.json
#         print(post_json)
#         user_id = post_json.get('user_id')
#         text = post_json.get('text')
#
#         if len(text) < 1 or len(text) > 100:
#             return jsonify(
#                 {"result": "NG", "message": "文字数が1から100文字でない"}
#                 )
#         # create_post(user_id, text)
#     except Exception as e:
#         print(e)
#     return jsonify({"result": "OK"})   # return flask.jsonify(res='error'), 400


# curl -H 'Accept:application/json' -H 'Content-Type:application/json' localhost:5000/posts/3372bb1e-8aa3-4ca1-ae78-53da089345bb/comments
# @app.route('/posts/<string:post_id>/comments', methods=['GET'])
# def get_comments(post_id):
#     # 投稿へのコメント一覧
#     # json = request.get_json()
#     # request.args.get('test', '')
#     comments = read_comments(post_id)
#     return jsonify({"comments": comments})


# curl -X POST -H 'Content-Type:application/json' -d '{"user_id": "1", "text": "hoge"}' localhost:5000/posts/3372bb1e-8aa3-4ca1-ae78-53da089345bb/comments/create
@app.route('/upload', methods=['POST'])
def post_comment():
    if 'sound' not in request.files:
        make_response(jsonify({'result': 'sound is required.'}))

    file = request.files['sound']
    fileName = file.filename
    if '' == fileName:
        make_response(jsonify({'result':'filename must not empty.'}))

    saveFileName = datetime.now().strftime("%Y%m%d_%H%M%S_") \
        + werkzeug.utils.secure_filename(fileName)
    file.save(os.path.join(UPLOAD_DIR, saveFileName))
    return make_response(jsonify({'result':'upload OK.'}))


@app.errorhandler(werkzeug.exceptions.RequestEntityTooLarge)
def handle_over_max_file_size(error):
    print("werkzeug.exceptions.RequestEntityTooLarge")
    return 'result : file size is overed.'


if __name__ == "__main__":

    app.run(debug=True)

