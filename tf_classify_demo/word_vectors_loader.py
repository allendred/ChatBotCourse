"""
词向量加载器
"""
# coding:utf-8

import sys
import struct
import numpy as np

MAX_W = 50
FLOAT_SIZE = 4

def get_words_sizes(file_name):
    """
    获取词向量文件的词数和维度
    """
    with open(file_name, "rb") as input_file:
        # 获取词表数目及向量维度
        words_and_size = input_file.readline()
        words_and_size = words_and_size.strip()
        words = int(words_and_size.decode('utf-8').split(' ')[0])
        size = int(words_and_size.decode('utf-8').split(' ')[1])
    return words, size


def load_vectors(file_name):
    """
    加载向量文件
    """
    print("begin load vectors")

    with open(file_name, "rb") as input_file:
        # 获取词表数目及向量维度
        words_and_size = input_file.readline()
        words_and_size = words_and_size.strip()
        words = int(words_and_size.decode('utf-8').split(' ')[0])
        size = int(words_and_size.decode('utf-8').split(' ')[1])
        print("words =", words)
        print("size =", size)

        word_vector_dict = {}
        word_id_dict = {}

        for word_id in range(words):
            word = b''
            # 读取一个词
            while True:
                charactor = input_file.read(1)
                if charactor is False or charactor == b' ':
                    break
                word = word + charactor
            word = word.strip()

            # 读取词向量
            vector = np.empty([size])
            for index in range(size):
                weight_str = input_file.read(FLOAT_SIZE)
                (weight,) = struct.unpack('f', weight_str)
                vector[index] = weight

            # 将词及其对应的向量存到dict中
            word_vector_dict[word] = vector
            word_id_dict[word] = word_id

    print("load vectors finish")
    return word_vector_dict, word_id_dict

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ", sys.argv[0], "vectors.bin")
        sys.exit(-1)
    WORD_VECTOR_DICT, WORD_ID_DICT = load_vectors(sys.argv[1])
    print(WORD_VECTOR_DICT['数学'.encode('utf-8')])
