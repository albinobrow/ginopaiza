#!/usr/bin/env python
# coding: UTF-8

import sys
if sys.version_info[0]<3: input=raw_input

class StandardInput:

    def stdin_string(self):
        self.s=str(input().rstrip())
        return self.s

    def stdin_integer(self):
        self.n=int(input().rstrip())
        return self.n

    def stdin_array(self):
        self.arr=input().rstrip().split()
        return self.arr

    def stdin_integer_array(self):
        self.arr=list(map(int,input().rstrip().split()))
        return self.arr

def test(n, arr):
    m,a,b=arr
    if n>=m:
        return n*a
    else:
        return n*b

if __name__ == '__main__':
    obj=StandardInput()
    n=obj.stdin_integer()
    arr=obj.stdin_integer_array()
    print(test(n,arr))
