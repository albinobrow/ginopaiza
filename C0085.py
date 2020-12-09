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

def test(arr, s):
    r=""
    for i in s:
        j=ord(i)-97
        if arr[j] > 0:
            r+=i
            arr[j]-=1
    return r

def main():
    obj=StandardInput()
    arr=obj.stdin_integer_array()
    s=obj.stdin_string()
    print(test(arr, s))

if __name__ == '__main__':
    main()
