# -*- coding: utf-8 -*-
import multiprocessing
from gensim.models import Doc2Vec


if __name__ == '__main__':

    outp1 = "E:\zh_cnn_text_classify\data\ham_100.utf8', 'r', encoding='UTF-8'"
    outp2 = "D:/dataset/quora/vector_english/quora_duplicate_question_word2vec_100.vector"
    outp3 = "D:/dataset/quora/vector_english/quora_duplicate_question_doc2vec_100.vector"

    model = Doc2Vec(size=100, window=5, min_count=0, workers=multiprocessing.cpu_count(), dm=0,
                    hs=0, negative=10, dbow_words=1, iter=10)

    # trim unneeded model memory = use(much) less RAM
    # model.init_sims(replace=True)
    model.save(outp1)  # save dov2vec model
    model.wv.save_word2vec_format(outp2, binary=False)  # save word2vec向量
    # 保存doc2vector向量
    outid = open(outp3, 'w')
    print("doc2vecs length:", len(model.docvecs))
    for id in range(len(model.docvecs)):
        outid.write(str(id)+"\t")
        for idx, lv in enumerate(model.docvecs[id]):
            outid.write(str(lv)+" ")
        outid.write("\n")

    outid.close()
