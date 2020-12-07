#!/usr/bin/env python
# coding: UTF-8

import sys
import numpy as np
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

    def stdin_integer_array(n):
        self.arr=list(map(int,input().rstrip().split()))
        return self.arr

def test(arr):
    return np.prod(np.array(arr))

def main():
    obj=StandardInput()
    arr=[]
    [arr.append(obj.stdin_integer()) for i in range(2)]
    print(test(arr))

if __name__ == '__main__':
    main()
