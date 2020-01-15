import fasttext
import jieba
from utils import preprocess

model = fasttext.load_model('model/1579082291.model')

text = ' 澳洲毕业证【Q/微457202606】新西兰怀卡托大学学位证成绩单/办澳洲新西兰怀卡托大学毕业证成绩单/官方学历认证本科/硕士 (The University of Waikato'
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