# -*- coding: utf-8 -*-
import jieba
import xlrd
import os
from utils import preprocess


def get_dataset(raw_path, output_file):
    wb = xlrd.open_workbook(raw_path)
    sheet = wb.sheet_by_index(0)
    for i in range(sheet.nrows):
        label = sheet.cell_value(i, 0)
        # 定义excel中的1代表广告书，label为1
        # 定义excel中的非1代表非广告书，label为2
        if label == 1:
            label_text = '\t__label__1'
        else:
            label_text = '\t__label__2'
        content = sheet.cell_value(i, 1)
        content = str(content).replace('\n', ' ').replace('\t', ' ')
        content = preprocess.get_processed_text([content])
        content = jieba.cut(content)
        content = ' '.join(content)
        content = content
        content = content + label_text + '\n'
        # 写入
        output_file.write(content)
    output_file.flush()
    output_file.close()


# 相对路径
basedir = "./data"
# 训练集和测试集在excel手动整理, 比例7:3或8:2
raw_train = basedir + '/train.xlsx'
raw_test = basedir + '/test.xlsx'

# 生成fastext的训练和测试数据集
ftrain = open(basedir + "/ad_fasttext_train.txt", "w", encoding="utf-8")
ftest = open(basedir + "/ad_fasttext_test.txt", "w", encoding="utf-8")

# 生成训练集
get_dataset(raw_train, ftrain)

# 生成测试集
get_dataset(raw_test, ftest)

print('训练完成')


