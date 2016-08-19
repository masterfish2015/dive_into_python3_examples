#!/usr/bin/python3
# -*- coding: utf-8 -*-
line_number = 0
with open('chinese.txt', encoding='utf-8') as afile:
    for aline in afile:
        line_number += 1
        print('{:>4}:{}'.format(line_number, aline.rstrip()))
