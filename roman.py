#!/usr/bin/python3
# -*- coding: utf-8 -*-

roman_numeral_map = (
    ('M',1000),
    ('CM',900),
    ('D',500),
    ('CD',400),
    ('C',100),
    ('XC',90),
    ('L',50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I',1))

class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass

def to_roman(n):
    '''convert integer to Roman numeral '''
    if not (0<n<4000):
        raise OutOfRangeError('must be 1..3999')

    if not isinstance(n, int):
        raise NotIntegerError('non-integers can not be converted')

    result = ''
    for numeral, integer in roman_numeral_map:
        while n>= integer:
            result += numeral
            n -= integer
            #print('{0} from input, adding {1} to output ({2}).'.format(integer, numeral, n))
    return result
