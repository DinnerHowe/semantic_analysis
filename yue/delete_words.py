#!/usr/bin/env python
#coding=utf-8
"""
this code is writen for yue

Copyright (c) 2017 Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify

"""

from lanLib import words

class delet_words():
    def __init__(self):
        self.define()
        self.Delete()

    def define(self):
        ######################################
        ## 手动输入对应文件位置，取消注释这里
        ######################################
        # self.outfile = raw_input('请输入写入文件的地址（eg：**/**/new.txt）： ')
        # self.infile = raw_input('请输入读取文件的地址（eg：**/**/old.txt）： ')
        # self.key_words_file = raw_input('请输入关键词文件的地址（eg：**/**/words.txt）： ')

        ######################################
        ## 手动输入对应文件位置，注释这里
        ######################################
        self.outfile ='/home/howe/yue/test/new.txt'
        self.infile = '/home/howe/yue/test/input.txt'
        self.key_words_file = '/home/howe/yue/test/key_word.txt'

        self.key_words = words.get_words(self.key_words_file)

    def Delete(self):
        words.delet_key_words(self.infile, self.outfile, self.key_words)


if __name__=='__main__':
    try:
        delet_words()
    except:
        print ' \033[1;31;31m oops error coming \033[0m'