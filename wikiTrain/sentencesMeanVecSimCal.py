# -*- coding: utf-8 -*-
import warnings
import jieba
from gensim.models import Word2Vec
import numpy as np

warnings.filterwarnings("ignore")

model = Word2Vec.load("wiki.zh.text.model")


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


def retMeanVec(seg):
    seg_list = seg.split()
    tmp = np.zeros((400,))
    for item in seg_list:
        try:
            tmp += model[item]
        except KeyError:
            pass
    return tmp / len(seg_list)


if __name__ == '__main__':
    s1 = '北京xxx公司'
    s2 = '北京xxxx有限公司'
    s3 = '广东明骏智能科技有限公司'
    seg1, seg2, seg3 = seg_sentence(s1), seg_sentence(s2), seg_sentence(s3)
    np1, np2, np3 = retMeanVec(seg1), retMeanVec(seg2), retMeanVec(seg3)
    print(np.dot(np1, np2) / (np.dot(np1, np1) ** 0.5 * (np.dot(np2, np2) ** 0.5)))
    print(np.dot(np1, np3) / (np.dot(np1, np1) ** 0.5 * (np.dot(np3, np3) ** 0.5)))
    # print(seg1, type(seg1))
    # print(retMeanVec(seg1))
