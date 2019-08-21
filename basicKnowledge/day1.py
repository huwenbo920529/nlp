# -*- coding:utf-8 -*-

# reference:https://www.tuicool.com/articles/QV36ru
# 算法实现：
# 基于Trie树结构实现高效的词图扫描，生成句子中汉字所有可能成词情况所构成的有向无环图（DAG)
# 采用了动态规划查找最大概率路径, 找出基于词频的最大切分组合
# 对于未登录词，采用了基于汉字成词能力的HMM模型，使用了Viterbi算法

# 功能 1)：分词
# jieba.cut方法接受两个输入参数: 1) 第一个参数为需要分词的字符串 2）cut_all参数用来控制是否采用全模式
# jieba.cut_for_search方法接受一个参数：需要分词的字符串,该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细
# 注意：待分词的字符串可以是gbk字符串、utf-8字符串或者unicode
# jieba.cut以及jieba.cut_for_search返回的结构都是一个可迭代的generator，
# 可以使用for循环来获得分词后得到的每一个词语(unicode)，也可以用list(jieba.cut(...))转化为list
# 可以通过jieba.lcut()或者jieba.lcut_for_search()获得分词后的列表，列表中每个元素为unicode类型
import jieba.analyse
import jieba.posseg as pseg


print(jieba.lcut('我来到xxx大学'))
seg_list = jieba.cut('我来到xxx大学')  # 默认模式为cut_all=False,是精确模式
# print type(seg_list) #<type 'generator'>,可以用seg_list.next()获取每一个词
for item in seg_list:
    print(item, type(item), len(item))
print(u'默认模式（精确模式）:' + '/'.join(seg_list))  # 由于每个分词是unicode，所以前面的字符串连接时要加u，这是因为“”里面的汉字是按照ASCII码来编码的。

seg_list = jieba.cut('我来到天津工业大学', cut_all=True)
print(u'全模式:' + '|'.join(seg_list))

seg_list = jieba.cut_for_search('小明硕士毕业于中国科学院计算所，后在日本京都大学深造！')
print(u'搜索引擎模式:' + '#'.join(seg_list))

print('\n')
# 功能 2) ：添加自定义词典
# 开发者可以指定自己自定义的词典，以便包含jieba词库里没有的词。虽然jieba有新词识别能力，但是自行添加新词可以保证更高的正确率
# 词典格式和dict.txt一样，一个词占一行；每一行分三部分，一部分为词语，另一部分为词频，最后为词性（可省略），用空格隔开
# 方式：（1）可以用jieba.load_userdict(filename)加载用户字典
# （2）少量词汇可以自己用下面的方法添加：
# add_word(word,fre=None,tag=None)和del_word(word)在程序中动态的修改词
# 用suggest_freq(segment,tune=True)可调节单个词语的词频，使其能（或不能）被分出来
test_sent = "李小福是创新办主任也是云计算方面的专家;"
test_sent += "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类型"
words = jieba.cut(test_sent)
print(u'不加自定义字典：' + '/'.join(words))

jieba.load_userdict('myDict.txt')
words = jieba.cut(test_sent)
print(u'加入自定义字典：' + '/'.join(words))

print('/'.join(jieba.cut('如果放到旧字典中将出错。', HMM=False)))  # 这里要将HMM设置为False，默认为True
jieba.suggest_freq(('中', '将'), tune=True)
print('/'.join(jieba.cut('如果放到旧字典中将出错。', HMM=False)))  # 这里要将HMM设置为False，默认为True

print('\n')
# 功能 3) ：关键词提取
# 需要先import jieba.analyse，调用方法为：jieba.analyse.extract_tags(sentence,topK)
# 其中，setence为待提取的文本；topK为返回几个TF/IDF权重最大的关键词，默认值为20
# 返回一个list，且list中每个元素是一个unicode类型,若withWeight=True则list中每个元素是一个tuple


content = open('extractTags.txt', encoding='UTF-8').read()
tags = jieba.analyse.extract_tags(sentence=content, topK=10, withWeight=True, withFlag=False, allowPOS=0)
print(type(tags), type(tags[0]), tags[0])
for w, weight in tags:
    print(w, weight)
# print ','.join(tags)


print('\n')
# 功能 4) : 词性标注
# 需要先import jieba.posseg,
# 返回的也是个可迭代的generator，每个词是一个<class 'jieba.posseg.pair'>


result = pseg.cut('我爱天安门!')  # 返回的也是个可迭代的generator，每个词是一个<class 'jieba.posseg.pair'>，而jieba.cut()每个词是一个unicode类型的。
for w in result:
    print(w.word + '(' + w.flag + ')', )  # 每个词是一个jieba.posseg.pair类对象，可以获得word词本身，也可以获得flag词性

    # 功能 5) : 并行分词
    # 原理：将目标文本按行分隔后，把各行文本分配到多个python进程并行分词，然后归并结果，从而获得分词速度的可观提升
    # 基于python自带的multiprocessing模块，目前暂不支持windows
    # 用法：jieba.enable_parallel(4) # 开启并行分词模式，参数为并行进程数
    # jieba.disable_parallel() # 关闭并行分词模式
    # import time
    # jieba.enable_parallel(4)
    # content = open('extract_tags.txt').read()
    # t1 = time.time()
    # words = list(jieba.cut(content))
    # t2 = time.time()
    # tm_cost = t2-t1
    # log_f = open("1.log","wb")
    # for w in words:
    #     print log_f, w.encode("utf-8"), "/" ,
    # print 'speed' , len(content)/tm_cost, " bytes/second"
