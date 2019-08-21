# _*_coding:utf-8_*_
import warnings
import jieba
warnings.filterwarnings("ignore")

seg_list = jieba.cut("北京xxxx有限公司")
print(list(seg_list))
print("defualt:", '/'.join(seg_list))

print('\nTfidf:')
from gensim import models, similarities

corpus = [[(0, 1.0), (1, 1.0), (2, 1.0)],
          [(2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0), (8, 1.0)],
          [(1, 1.0), (3, 1.0), (4, 1.0), (7, 1.0)],
          [(0, 1.0), (4, 2.0), (7, 1.0)],
          [(3, 1.0), (5, 1.0), (6, 1.0)],
          [(9, 1.0)], [(9, 1.0), (10, 1.0)],
          [(9, 1.0), (10, 1.0), (11, 1.0)],
          [(8, 1.0), (10, 1.0), (11, 1.0)]]
tfidf = models.TfidfModel(corpus)
vec = [(0, 1), (4, 1)]
sim = tfidf[vec]
index = similarities.MatrixSimilarity(tfidf[corpus], num_features=12)
sims = index[tfidf[vec]]
print(list(enumerate(sims)))

print('\n')
from gensim import corpora

documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]
print(texts)
# remove words that appear only once
from collections import defaultdict

frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
         for text in texts]
# print(texts)
from pprint import pprint  # pretty-printer

pprint(texts)

print('\ndictionary:')
dictionary = corpora.Dictionary(texts)
print(type(dictionary))
print(dictionary.token2id)
print(dictionary.dfs)
