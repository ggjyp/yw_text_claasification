# -*- coding: utf-8 -*-
import sys
import fasttext
import jieba
from flask import Flask, request, jsonify
from flask_cors import CORS

from utils import preprocess


app = Flask(__name__)
CORS(app)


@app.route('/text_classify')
def hello_world():
    text = request.args.get("text")
    if preprocess.have_chinese(text):
        # 包含中文，则只保留中文后并且对中文进行分词
        content = preprocess.get_chinese_preprocessed_text(text)
    else:
        content = 's'
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
