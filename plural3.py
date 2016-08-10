#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re


def build_match_and_apply_function(pattern, search, replace):
    def match_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return match_rule, apply_rule

patterns = \
    (
        (r'[sxz]$', '$', 'es'),
        (r'[^aeioudgkprt]h', '$', 'es'),
        (r'[^aeiou]y$', 'y$', 'ies'),
        (r'$', '$', 's')
    )
rules = [build_match_and_apply_function(pattern, search, replace) for (pattern, search, replace) in patterns]


def plural(noun):
    for match_rule, apply_rule in rules:
        if match_rule(noun):
            return apply_rule(noun)


if __name__ == "__main__":
    print(plural("agency"))
    print(plural("boy"))
    print(plural("rule"))
