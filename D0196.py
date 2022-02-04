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

def test(arr):
    return sum(arr)

def main():
    arr=[]
    obj=StandardInput()
    n=obj.stdin_integer()
    for i in range(n):
        arr.append(obj.stdin_integer())
    print(test(arr))

if __name__ == '__main__':
    main()
