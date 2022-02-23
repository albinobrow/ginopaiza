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

def test(n,m):
    if n+m==21:
        return "Win"
    else:
        return n+m

def main():
    obj=StandardInput()
    n=obj.stdin_integer()
    m=obj.stdin_integer()
    print(test(n,m))

if __name__ == '__main__':
    main()
