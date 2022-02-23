#!/usr/bin/env python
# coding: utf-8


def test():
    arr=[]
    n=int(input().rstrip())
    [arr.append(input().rstrip()) for i in range(n)]
    return arr

if __name__ == '__main__':
    print(*test())
