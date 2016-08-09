#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

def match_sxz(noun):
    '''查找匹配以sxz结尾的名词
    '''
    return re.search(r'[sxz]$', noun)

def apply_sxz(noun):
    '''将sxz结尾的名词改为复数
    '''
    return re.sub(r'$', 'es', noun)

def match_h(noun):
    '''查找匹配以h结尾且h发音的名词
    '''
    return re.search(r'[^aeioudgkprt]h$',noun)

def apply_h(noun):
    '''将以h结尾并且h发音的名词转为复数
    '''
    return re.sub(r'$', 'es', noun)

def match_y(noun):
    '''查找匹配以y结尾并且y发i的音的名词
    '''
    return re.search(r'[^aeiou]y$', noun)

def apply_y(noun):
    '''将以y结尾并且y发i的音的名词转换为复数
    '''
    return re.sub(r'y$', 'ies', noun)

def match_default(noun):
    '''匹配缺省的名词
    '''
    return True

def apply_default(noun):
    '''将缺省的名词转换为复数
    '''
    return noun+'s'

rules = ((match_sxz, apply_sxz),
         (match_h, apply_h),
         (match_y, apply_y),
         (match_default, apply_default)
         )

def plural(noun):
    '''函数功能，将传入的名词noun转换为复数形式
    '''
    for match_rule, apply_rule in rules:
        if match_rule(noun):
            apply_rule(noun)
