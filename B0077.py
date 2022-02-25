#!/usr/bin/env python
# coding: UTF-8

import copy, sys, numpy as np
if sys.version_info[0]<3: input=raw_input

class StandardInput:

    def stdin_string(self):
        self.s=str(input().rstrip())
        return self.s

    def stdin_integer(self):
        self.n=int(input().rstrip())
        return self.n
    
    def stdin_float(self):
        self.f=float(input().rstrip())
        return self.f 

    def stdin_array(self):
        self.arr=input().rstrip().split()
        return self.arr

    def stdin_integer_array(self):
        self.arr=list(map(int,input().rstrip().split()))
        return self.arr

def dice(n):
    return 7-n

def test(n,h,w,l,s):
    x,y=np.array(l)-1
    arr=np.array([[0]*w]*h)
    arr[x][y]=6
    t=1
    brr=[2,3,1,4,6,5]
    crr=[0]*6
    for i in s:
        if i == "U":
            crr=copy.copy(brr)
            if x-1>-1:
                x-=1
                crr[2]=brr[5]
                crr[4]=brr[0]
                crr[0]=brr[2]
                crr[5]=brr[4]
                brr=copy.copy(crr)
                arr[x][y]=brr[4]
        elif i == "D":
            crr=copy.copy(brr)
            if x+1<h:
                x+=1
                crr[2]=brr[0]
                crr[4]=brr[5]
                crr[0]=brr[4]
                crr[5]=brr[2]
                brr=copy.copy(crr)
                arr[x][y]=brr[4]
        elif i == "L":
            crr=copy.copy(brr)
            if y-1>-1:
                y-=1
                crr[2]=brr[3]
                crr[3]=brr[4]
                crr[1]=brr[2]
                crr[4]=brr[1]
                brr=copy.copy(crr)
                arr[x][y]=brr[4]
        elif i == "R":
            crr=copy.copy(brr)
            if y+1<w:
                y+=1
                crr[2]=brr[1]
                crr[3]=brr[2]
                crr[1]=brr[4]
                crr[4]=brr[3]
                brr=copy.copy(crr)
                arr[x][y]=brr[4]
    return arr

def main():
    obj=StandardInput()
    n,h,w=obj.stdin_integer_array()
    l=obj.stdin_integer_array()
    s=obj.stdin_string()
    for i in test(n,h,w,l,s):
        print(*i)

if __name__ == '__main__':
    main()
