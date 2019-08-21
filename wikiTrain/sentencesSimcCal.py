# -*- coding: utf-8 -*-
import warnings
import jieba
from gensim.models import Word2Vec

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


def match_reverse(seg1, seg2):
    results = []
    kks = 0
    global model
    if len(seg1) == 0:
        return 0
    for s in seg2:
        result = 0
        for d in seg2:
            # print(s, d)
            try:
                # print(model.similarity(s, d))
                result = max(model.similarity(s, d), result)
            except KeyError:
                if d == 2:
                    result += 1
        results.append(result)
    for kk in results:
        kks = kks + kk
    return kks / len(seg1)


def match_two_sentences(seg1, seg2):
    return match_reverse(seg1, seg2) + match_reverse(seg2, seg1) / 2


if __name__ == '__main__':
    s1 = '我来到北京大学！'
    s2 = '我去北京大学！'
    s3 = '我参观清华大学！'
    seg1, seg2, seg3 = seg_sentence(s1), seg_sentence(s2), seg_sentence(s3)
    print('{}与{}相似度：'.format(s1, s2), match_two_sentences(seg1, seg2))
    print('{}与{}相似度：'.format(s1, s3), match_two_sentences(seg1, seg3))
