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
        self.arr=list(input().rstrip())
        return self.arr

    def stdin_integer_array(self):
        self.arr=list(map(int,input().rstrip().split()))
        return self.arr

def test(x,y):
        if x < y:
            return abs(x-y)
        else:
            return 'Thank you'

if __name__ == '__main__':
    obj=StandardInput()
    x,y=[obj.stdin_integer() for i in range(2)]
    print(test(x,y))
