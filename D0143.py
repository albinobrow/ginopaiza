#!/usr/bin/env python
# coding: utf-8


def test():
    m,v,f=list(map(int,input().rstrip().split()))
    return int( 0.5*m*v**2*f**-1 )

if __name__ == '__main__':
    print(test())
