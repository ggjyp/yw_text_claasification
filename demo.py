# -*- coding: utf-8 -*-
import sys
import fasttext
from utils import preprocess
import jieba
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/text_classify')
def hello_world():
    text = request.args.get("text")
    content = preprocess.get_processed_text([text])
    content = jieba.cut(content)
    content = " ".join(content)
    print("content:", content)
    result = model.predict(content)
    label = result[0][0]
    score = result[1]
    if label == '__label__1':
        label = '广告书'
    else:
        label = '非广告书'
    res = {"label": label, "score": score[0]}
    print("result:", res)
    return jsonify(res)


if __name__ == "__main__":
    model_path = 'model/my_model.bin'
    if len(sys.argv) == 2:
        model_path = 'model/' + sys.argv[1]
    model = fasttext.load_model(model_path)
    app.run(host='0.0.0.0', port=13000)
