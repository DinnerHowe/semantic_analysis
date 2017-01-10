#!/usr/bin/env python
# coding=utf-8
"""
this code is writen for yue

Copyright (c) 2017 Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify

"""
import re

def delet_key_words(r_file, w_file, key_words):
    ##############################################
    # 删除目标文本中指定单词，并且按顺序合成输出到w_file
    # r_file : 是需要处理的文件
    # w_file : 是处理后写入输出的文件
    # key_words : 是等待删除的关键字
    ##############################################
    sentence = []
    with open(w_file, 'w') as f:
        content=[[''  if i.lower() in key_words else sentence.append(' '+i) for i in re.split('[ \n]', line)] for line in open(r_file).readlines()]
        #content 是处理之后的1维数组（输出的就是这个句子）
        #sentence 是处理之后的2维数组
        f.writelines(sentence)


def get_words(file):
    ##############################################
    # 输出需要删除的单词组
    ##############################################
    words = []
    with open(file, 'r') as f:
        [words.extend(re.split('[ \n]', i)) for i in f.readlines()]
        return [j for j in words if j != '']