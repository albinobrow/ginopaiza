#!/usr/bin/env python
# coding: UTF-8

import numpy, sys
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

def test(arr, bread, price):
    price, bread=numpy.array(price), numpy.array(bread)
    for i in arr:
        demand=numpy.array(list(map(int, i[1:])))
        if i[0]=='buy':
            if numpy.all(bread >= demand):
                bread-=demand
                print(sum(price*demand))
            else:
                print(-1)
        else:
            bread+=demand

if __name__ == '__main__':
    obj=StandardInput()
    arr, bread, price=[],[],[]
    n,q=obj.stdin_integer_array()
    for i in range(n):
        a,b=obj.stdin_integer_array()
        price.append(a)
        bread.append(b)
    [arr.append(obj.stdin_array()) for i in range(q)]
    test(arr, bread, price)
