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
    
def delay(n,d,a):
    s=100//n*a
    if d > 9:
        return 0
    elif d > 0:
        return int(s*0.8)
    else:
        return s

def evaluation(a):
    if a < 60:
        return 'D'
    elif a < 70:
        return 'C'
    elif a < 80:
        return 'B'
    else:
        return 'A'

if __name__ == '__main__':
    arr=[]
    obj=StandardInput()
    k,n=obj.stdin_integer_array()
    [arr.append(obj.stdin_integer_array()) for i in range(k)]
    [print(evaluation(delay(n,d,a))) for d,a in arr]
