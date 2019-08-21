# -*- coding: utf-8 -*-


def stop_wd_reduction(in_file_path, out_file_path):
    infile = open(in_file_path, 'r', encoding='utf-8')
    outfile = open(out_file_path, 'w', encoding='utf-8')
    stop_words_list = []
    for s in infile.read().split('\n'):
        if s not in stop_words_list:
            stop_words_list.append(s)
            outfile.write(s + '\n')


stop_wd_reduction('stopwords.txt', 'stopword.txt')