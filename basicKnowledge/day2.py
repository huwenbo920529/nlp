# encoding:UTF-8
# TFIDF的主要思想是：如果某个词或短语在一篇文章中出现的频率TF高，并且在其他文章中很少出现，
# 则认为此词或者短语具有很好的类别区分能力，适合用来分类。TFIDF实际上是：TF * IDF，
# TF词频(Term Frequency)，IDF逆向文件频率(Inverse Document Frequency)。
# TF表示词条在文档d中出现的频率。
# IDF的主要思想是：如果包含词条t的文档越少，也就是n越小，IDF越大，则说明词条t具有很好的类别区分能力。
# 如果某一类文档C中包含词条t的文档数为m，而其它类包含t的文档总数为k，显然所有包含t的文档数n=m+k，当m大的时候，n也大，
# 按照IDF公式得到的IDF的值会小，就说明该词条t类别区分能力不强。
#   假如一篇文件的总词语数是100个，而词语“母牛”出现了3次，那么“母牛”一词在该文件中的词频就是3/100=0.03。
#   一个计算文件频率 (IDF) 的方法是测定有多少份文件出现过“母牛”一词，然后除以文件集里包含的文件总数。
#   所以，如果“母牛”一词在1,000份文件出现过，而文件总数是10,000,000份的话，其逆向文件频率就是 log(10,000,000 / 1,000)=4。
#   最后的TF-IDF的分数为0.03 * 4=0.12。

import jieba.analyse

data = open('NBA.txt', encoding='UTF-8').read()
print(' '.join(jieba.analyse.extract_tags(data, topK=20, withWeight=False, allowPOS=())))

data = open(u'西游记.txt', encoding='UTF-8').read()
print(' '.join(jieba.analyse.extract_tags(data, topK=20, withWeight=False, allowPOS=())))
# print len(jieba.lcut(data))

print('\n')
# TextRank最初是作为关键词抽取方法提出来的，后来也有人尝试作为权重计算方法，
# 但需要注意的是TextRank的计算复杂度很高，所以不建议实用中采用该算法。
# (1)把给定的文本T按照完整句子进行分割，即T=[S1,S2,S3,...,Sm]
# (2)对于每个句子，进行分词和词性标注处理，并过滤掉停用词，只保留指定词性的单词，如名词、动词、形容词，
# 即Si=[ti,1 ,ti,2 ti,3,...,ti,n]，其中 ti,j 是保留后的候选关键词。
# (3)构建候选关键词图G = (V,E)，其中V为节点集，由（2）生成的候选关键词组成，
# 然后采用共现关系（co-occurrence）构造任两点之间的边，两个节点之间存在边仅当它们对应的词汇在长度为K的窗口中共现，
# K表示窗口大小，即最多共现K个单词。
# (4)根据上面公式，迭代传播各节点的权重，直至收敛。
# (5)对节点权重进行倒序排序，从而得到最重要的T个单词，作为候选关键词。
# (6)由5得到最重要的T个单词，在原始文本中进行标记，若形成相邻词组，则组合成多词关键词。
lines = open('NBA.txt', encoding='UTF-8').read()
print("  ".join(jieba.analyse.textrank(lines, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))))
lines = open('NBA.txt', encoding='UTF-8').read()
print("  ".join(jieba.analyse.textrank(lines, topK=20, withWeight=False, allowPOS=('ns', 'n'))))

print('\n')
# Tokenize：返回词语在原文的起止位置
# 注意，输入参数只接受 unicode
# 返回的是一个迭代器，迭代器中每个元素是一个元组，元组结构为（unicode,int,int）
print("这是默认模式的tokenize")
result = jieba.tokenize(u'自然语言处理非常有用')
for tk in result:
    print("%s\t\t start: %d \t\t end:%d" % (tk[0], tk[1], tk[2]))

print("这是搜索模式的tokenize")
result = jieba.tokenize(u'自然语言处理非常有用', mode='search')
for tk in result:
    print("%s\t\t start: %d \t\t end:%d" % (tk[0], tk[1], tk[2]))
