#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


def build_match_and_apply_functions(pattern, search, replace):
    def match_rule(word):
        return re.search ( pattern, word )

    def apply_rule(word):
        return re.sub ( search, replace, word )

    return match_rule, apply_rule


class LazyRules:
    rules_filename = "plural4-rules.txt"

    def __init__(self):
        self.pattern_file = open ( self.rules_filename, encoding='utf-8' )
        self.cache = []

    def __iter__(self):
        self.cache_index = 0
        return self

    def __next__(self):
        self.cache_index += 1
        if len ( self.cache ) >= self.cache_index:
            return self.cache[self.cache_index - 1]

        if self.pattern_file.closed:
            raise StopIteration

        line = self.pattern_file.readline ( )
        if not line:
            self.pattern_file.close ( )
            raise StopIteration

        pattern, search, replace = line.split ( None, 3 )
        funcs = build_match_and_apply_functions ( pattern, search, replace )
        self.cache.append ( funcs )
        return funcs


rules = LazyRules ( )


def plural(noun):
    for match_rule, apply_rule in rules:
        if match_rule ( noun ):
            return apply_rule ( noun )
    raise ValueError ( 'no matching rule for {0}'.format ( noun ) )


if __name__ == "__main__":
    print ( plural ( "agency" ) )
    print ( plural ( "boy" ) )
    print ( plural ( "ash" ) )
    print ( plural ( "apple" ) )
