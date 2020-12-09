#!/usr/bin/env python
# coding: UTF-8

import sys, numpy as np
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

def test(arr,x,y):
    arr=np.array(arr)
    e=sorted(arr[:,0])[y-1]
    j=sorted(arr[:,1])[y-1]
    m=sorted(arr[:,2])[y-1]
    for i in arr:
        c=3
        if i[0]>e:
            c-=1
        if i[1]>j:
            c-=1
        if i[2]>m:
            c-=1
        print(c)

def main():
    obj=StandardInput()
    x,y=obj.stdin_integer_array()
    arr=[]
    [arr.append(obj.stdin_integer_array()) for i in range(x)]
    test(arr,x,y)

if __name__ == '__main__':
    main()
