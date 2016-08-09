#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

def plural(noun):
    '''函数功能，将传入的名词noun转换为复数形式
    '''
    if re.search(r'[sxz]$', noun):
        return re.sub('$', 'es', noun)
    elif re.search(r'[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)
    elif re.search(r'[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun+'s'
