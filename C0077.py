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
    
def delay(d,a):
    if d > 9:
        return 0
    elif d > 0:
        return int(100*a*0.8/n)
    else:
        return a*100//n

def evaluation(a):
    if a < 60:
        return 'D'
    elif a < 70:
        return 'C'
    elif a < 80:
        return 'B'
    else:
        return 'A'

def test(n,arr):
    for d,a in arr:
        print(evaluation(delay(d,a)))

if __name__ == '__main__':
    obj=StandardInput()
    k,n=obj.stdin_integer_array()
    arr=[]
    [arr.append(obj.stdin_integer_array()) for i in range(k)]
    test(n,arr)
