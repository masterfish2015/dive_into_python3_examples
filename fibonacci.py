#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Fib:
    """生成斐波那契数列"""

    def __init__(self, max_number):
        self.max = max_number

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


if __name__ == "__main__":
    fib = Fib ( 1000 )
    print ( fib.__doc__ )
    print ( fib.__class__ )
    for n in Fib ( 1000 ):
        print ( n, end=' ' )
