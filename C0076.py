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
    
def cost(s):
    if s > 22:
        return x*8+y*5+z*10
    elif s > 17:
        return x*8+y*(s-17)+z*9
    elif s > 9:
        return x*(s-9)+z*9
    else:
        return z*s

def test(x,y,z,arr):
    total=0
    for s,t in arr:
        total+=cost(t)-cost(s)
    return total

if __name__ == '__main__':
    obj=StandardInput()
    x,y,z=obj.stdin_integer_array()
    n=obj.stdin_integer()
    arr=[]
    [arr.append(obj.stdin_integer_array()) for i in range(n)]
    print(test(x,y,z,arr))
