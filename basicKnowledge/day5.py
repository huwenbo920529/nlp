# -*-conding:utf-8-*-
import warnings
# 引入分词工具
import jieba
from gensim.models import word2vec
warnings.filterwarnings("ignore")


# 引入日志配置
# import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# 引入数据集
raw_sentences = ["但由于中文没有像英文那么自带天然的分词", "所以我们第一步采用分词"]

# 切分词汇
sentences = []
for s in raw_sentences:
    tmp = []
    for item in jieba.cut(s):
        tmp.append(item)
    sentences.append(tmp)

print(sentences)
# 构建模型
print(sentences)
model = word2vec.Word2Vec(sentences, min_count=1)

# 进行词向量输出
print(model['中文'])
