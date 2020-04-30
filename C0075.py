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

def test(n,arr):
    p=0
    for i in arr:
        if i <= p:
            p-=i
        else:
            n-=i
            p+=i//10
        print(n,p)

if __name__ == '__main__':
    obj=StandardInput()
    arr=[]
    n,m=obj.stdin_integer_array()
    [arr.append(obj.stdin_integer()) for i in range(m)]
    test(n,arr)
