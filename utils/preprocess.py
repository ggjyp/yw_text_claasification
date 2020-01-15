def is_chinese(uchar):
    if u'\u4e00' <= uchar <= u'\u9fa5':
        return True
    else:
        return False


def format_str(raw_str):
    content_str = ''

    for i in raw_str:
        if is_chinese(i):
            content_str = content_str + i
    return content_str


def get_processed_text(content):
    chinese_list = []
    for line in content:
        chinese_list.append(format_str(line))
    return chinese_list[0]
