#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
@Author: Xinshuo Gu 
@Date: 2018-02-22 18:00:24  
@Last Modified by: Xinshuo Gu 
@Last Modified time: 2018-02-24 11:41:51 
'''

'''
Here defines all the function to make and combine
the string using map/reduce in order to send to telegram  
'''

from functools import reduce

def singleCombine(element1,element2):
    return element1 +'\n' + element2 +'\n'


def allCombine(element1,element2):
    #return element1  + '\n' + '-.-.'*10 + '\n' + '-.-.'*10 + '\n\n' + element2
    return element1  + '\n' + r'=.=.'*8 + '\n\n' + element2

def mapCombine(element1):
    return reduce(singleCombine,element1)


def sendText(stor_list):
    single_str_list = list(map(mapCombine,stor_list))
    all_str_list    = reduce(allCombine,single_str_list)
    return all_str_list


