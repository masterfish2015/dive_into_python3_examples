#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


def build_match_and_apply_functions(pattern, search, replace):
    def match_rule(word):
        return re.search ( pattern, word )

    def apply_rule(word):
        return re.sub ( search, replace, word )

    return match_rule, apply_rule


rules = []
with open ( 'plural4-rules.txt', encoding='utf-8' ) as pattern_file:
    for line in pattern_file:
        pattern, search, replace = line.split ( None, 3 )
        rules.append ( build_match_and_apply_functions ( pattern, search, replace ) )


def plural(noun):
    for match_rule, apply_rule in rules:
        if match_rule ( noun ):
            return apply_rule ( noun )


if __name__ == "__main__":
    print ( plural ( "agency" ) )
    print ( plural ( "boy" ) )
    print ( plural ( "rule" ) )
