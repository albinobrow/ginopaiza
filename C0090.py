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

def test(s):
    a=0
    for i in s:
        if i == 0:
            a+=12*2
        else:
            a+=(i+2)*2
    return a


def main():
    obj=StandardInput()
    s=list(map(int, list(''.join(obj.stdin_string().split('-')))))
    print(test(s))

if __name__ == '__main__':
    main()
