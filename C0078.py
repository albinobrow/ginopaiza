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

def test(n,c1,c2,arr):
    s,t=0,0
    for i in range(n):
        if arr[i] >= c2 or i==n-1:
            t+=arr[i]*s
            s=0
        elif arr[i] <= c1:
            t-=arr[i]*1
            s+=1
        else:
            pass
    return t

if __name__ == '__main__':
    obj=StandardInput()
    n,c1,c2=obj.stdin_integer_array()
    arr=[]
    [arr.append(obj.stdin_integer()) for i in range(n)]
    print(test(n,c1,c2,arr))
