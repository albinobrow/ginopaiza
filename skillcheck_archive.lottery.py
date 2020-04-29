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

def lottery(b,i):
    x=abs(b-i)
    if x==0:
        return 'first'
    elif x==1:
        return 'adjacent'
    elif x%10**4==0:
        return 'second'
    elif x%10**3==0:
        return 'third'
    else:
        return 'blank'

if __name__ == '__main__':
    obj=StandardInput()
    b=obj.stdin_integer()
    n=obj.stdin_integer()
    [print(lottery(b,obj.stdin_integer())) for i in range(n)]
