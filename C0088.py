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

def test(arr,brr,t,q):
    for i in range(q):
        p=arr[brr[i][0]-1]*brr[i][1]
        if p <= t:
            t-=p
    return t

def main():
    obj=StandardInput()
    n=obj.stdin_integer()
    arr=obj.stdin_integer_array()
    t,q=obj.stdin_integer_array()
    brr=[]
    for i in range(q):
        brr.append(obj.stdin_integer_array())
    print(test(arr,brr,t,q))

if __name__ == '__main__':
    main()
