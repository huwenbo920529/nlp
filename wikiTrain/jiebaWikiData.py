# -*- coding: utf-8 -*-
# jieba_wikiData.py将wiki数据用jieba进行分词，生成wiki.zh.text.seg文件
import jieba


# jieba.load_userdict('userdict.txt')
# 创建停用词list
def stop_words_list(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stop_words_list('stopwords.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords and word != '\t':
            outstr += word
            outstr += " "
    return outstr


inputs = open('wiki.zh.text', 'r', encoding='utf-8')
outputs = open('wiki.zh.text.seg', 'w', encoding='utf-8')
for line in inputs:
    line_seg = seg_sentence(line)  # 这里的返回值是字符串
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()
