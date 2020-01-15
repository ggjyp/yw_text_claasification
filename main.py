# _*_coding:utf-8 _*_
import fasttext
import time
from utils import preprocess
import jieba


model_name = int(time.time())
model_path = "model/" + str(model_name) + ".model"
# 训练模型
classifier = fasttext.train_supervised(input="data/ad_fasttext_train.txt")

# 测试模型
result = classifier.test("data/ad_fasttext_test.txt")
print(result)

# 保存模型
classifier.save_model(model_path)
print("保存模型完毕")
