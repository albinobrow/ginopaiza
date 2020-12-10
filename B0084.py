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

def test(arr,n,m,k):
    arr=np.array(arr)
    brr=[]
    for i in range(1,m+1):
        c=0
        for j in range(n):
            if arr[0,j]==arr[i,j]==3:
                c+=1
        if c>=k:
            for j in range(n):
                if arr[0,j]==0 and arr[i,j]==3:
                    brr.append(j+1)
    if brr == []:
        print("no")
    else:
        print(*sorted(set(brr)))


def main():
    obj=StandardInput()
    n,m,k=obj.stdin_integer_array()
    arr=[]
    [arr.append(obj.stdin_integer_array()) for i in range(m+1)]
    test(arr,n,m,k)

if __name__ == '__main__':
    main()
