import jieba
import re


def is_chinese(uchar):
    if u'\u4e00' <= uchar <= u'\u9fa5':
        return True
    else:
        return False


def have_chinese(content):
    for w in content:
        if is_chinese(w):
            return True
    return False


def format_str(raw_str):
    content_str = ''

    for i in raw_str:
        if is_chinese(i):
            content_str = content_str + i
    return content_str


def preprocess_chinese_text(content):
    chinese_list = []
    for line in content:
        chinese_list.append(format_str(line))
    return chinese_list[0]


def get_chinese_preprocessed_text(content):
    # 包含中文，则只保留中文后并且对中文进行分词
    content = str(content).replace('\n', ' ').replace('\t', ' ')
    content = preprocess_chinese_text([content])
    content = jieba.cut(content)
    content = " ".join(content)
    return content


def get_english_preprocessed_text(content):
    content = str(content).replace('\n', ' ').replace('\t', ' ')
    content = content.lower()  # Converting to lowercase
    cleaner = re.compile('<.*?>')
    content = re.sub(cleaner, ' ', content)  # Removing HTML tags
    content = re.sub(r'[?|!|\'|"|#]', r'', content)
    content = re.sub(r'[.|,|)|(|\|/]', r' ', content)  # Removing Punctuations
    return content
