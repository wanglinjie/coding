#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: Wanglj
Create Time  : 20160314
Last Modified: 
读取词向量
'''

import numpy as np
import chardet

# from util import Reader

class WordVectors(object):

    def __init__(self, embsize):
        self._vectors = np.array([[0]])
        self._word2id = {"OOV":0}
        self._embsize = embsize

        self.zero = np.zeros(self._embsize)

    def __len__(self):
        return len(self._word2id)

    def embsize(self):
        return self._embsize

    def __getitem__(self, index_or_index_array):
        # return self._vectors[:, index_or_index_array].copy()
        return self._vectors[index_or_index_array].copy()

    def get_word_index(self, word):
        return self._word2id.get(word, 0)

    @classmethod
    def load_vectors(cls, filename):
        '''
        Load word vectors from a file
    
        Args:
            filename: the name of the file that contains the word vectors
                Comment lines are started with #
                If the first line except comments contains only two integers, it's
                assumed that the first is the vocabulary size and the second is the 
                word embedding size (the same as word2vec).
        
        Return:
            a class of word vectors
        '''
        at_beginning = True
        with open(filename, "r") as f:
        # with Reader(filename) as f:
            idx = 1
            vectors = [[0]]
            word2id = {"OOV":0}

            for line in f:
                # try:
                #     line = line.decode(chardet.detect(line)["encoding"]).encode("utf-8")
                # except:
                #     line = line.decode("utf-8").encode("utf-8")
                if line.startswith("#"):
                    continue
                if at_beginning:
                    at_beginning = False
                    parts = line.strip().split()
                    if len(parts) == 2:
                        embsize = int(parts[1])
                        oov = np.zeros(embsize)
                    else:
                        word = parts[0]
                        vec = np.array([float(v) for v in parts[1:] if v != "" and v != " "], dtype=np.float64)
                        embsize = len(vec)
                        oov = np.zeros(embsize)
                        oov += vec
                        vectors.append(vec)
                        word2id[word] = idx
                else:
                    parts = line.strip().split(" ")
                    word = parts[0]
                    vec = np.array([float(v) for v in parts[1:] if v != "" and v != " "], dtype=np.float64)
                    assert(vec.size == embsize)
                    oov += vec
                    vectors.append(vec)
                    word2id[word] = idx
                    if idx == 0:
                        print "idx word is ", word
                    idx += 1
            oov = oov / (len(vectors) - 1)
            vectors[0] = oov

            word_vectors = WordVectors(embsize)
            word_vectors._vectors = np.array(vectors)
            word_vectors._word2id = word2id
            return word_vectors