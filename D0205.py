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
    
    def stdin_float(self):
        self.f=float(input().rstrip())
        return self.f 

    def stdin_array(self):
        self.arr=input().rstrip().split()
        return self.arr

    def stdin_integer_array(self):
        self.arr=list(map(int,input().rstrip().split()))
        return self.arr

def test(p,q):
    if p > q:
        return 1
    elif p < q:
        return 2

def main():
    obj=StandardInput()
    d,f=obj.stdin_integer_array()
    p=f/d
    d,f=obj.stdin_integer_array()
    q=f/d
    print(test(p,q))

if __name__ == '__main__':
    main()
