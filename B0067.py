#!/usr/bin/env python
# coding: UTF-8

import numpy, sys
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

def finish(arr):
    if sum(numpy.array(arr)[:,0])==0:
        return 'YES'
    else:
        return 'NO'

def test(s,t,arr):
    for i in range(s,t+1):
        for j in arr:
            if j[0]>0 and j[1]<=i and j[2]>=i:
                j[0]-=1
                break
    return finish(arr)

if __name__ == '__main__':
    obj=StandardInput()
    n=obj.stdin_integer()
    s,t,arr=1000,1,[]
    for i in range(n):
        a,b,c=obj.stdin_integer_array()
        if b<s:
            s=b
        if c>t:
            t=c
        arr.append([a,b,c])
    print(test(s,t,arr))
