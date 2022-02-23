#!/usr/bin/env python
# coding utf-8


from math import ceil

def test():
    n,x,y=list(map(int,input().rstrip().split()))
    return y*ceil(n*x**-1)

if __name__ == '__main__':
    print(test())
