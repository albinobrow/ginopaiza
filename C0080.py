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

def test(arr, n, y):
    p,q=0,0
    for i, j in enumerate(arr, 1):
        if i%n==j%n:
            p+=1
        else:
            q+=1
    if y > q:
        return p*1000
    else:
        return -1
    
def main():
    obj=StandardInput()
    n,y=obj.stdin_integer_array()
    m=obj.stdin_integer()
    arr=obj.stdin_integer_array()
    print(test(arr, n, y))

if __name__ == '__main__':
    main()
