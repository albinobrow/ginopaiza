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
    
    def stdin_float(self):
        self.f=float(input().rstrip())
        return self.f 

    def stdin_array(self):
        self.arr=input().rstrip().split()
        return self.arr

    def stdin_integer_array(self):
        self.arr=list(map(int,input().rstrip().split()))
        return self.arr

def test(n,k,arr):
    arr=np.array(sorted(arr))
    brr=list(map(abs,arr-k))
    crr=[i for i, x in enumerate(brr) if x == min(brr)]
    drr=[arr[x] for i, x in enumerate(crr)]
    return drr

def main():
    obj=StandardInput()
    n,k=obj.stdin_integer_array()
    arr=[]
    for i in range(n):
        t=obj.stdin_integer()
        arr.append(t)
    ans=test(n,k,arr)
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()
