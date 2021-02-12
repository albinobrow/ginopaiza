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

def test(n):
    while n!=n[::-1]:
        a=int(n[::-1])
        b=int(n)
        n=str(a+b)
    return n

def main():
    obj=StandardInput()
    n=obj.stdin_string()
    print(test(n))

if __name__ == '__main__':
    main()
