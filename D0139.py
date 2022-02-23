#!/usr/bin/env python
# coding: utf-8

class StandardInput:

    def stdin_integer(self):
        self.n=int(input().rstrip())
        return self.n

    def stdin_array(self):
        self.arr=input().rstrip().split()
        return self.arr

def lessWin(n, arr):
    gcount,pcount=0,0
    for i in range(n):
        if arr[i] == "G":
            gcount+=1
        else:
            pcount+=1
    if gcount < pcount:
        return "G"
    elif gcount > pcount:
        return "P"
    else:
        return "Draw"

if __name__ == '__main__':
    obj=StandardInput()
    n=obj.stdin_integer()
    arr=obj.stdin_array()
    print(lessWin(n, arr))
