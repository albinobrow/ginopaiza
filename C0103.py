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
    
    def stdin_float(self):
        self.f=float(input().rstrip())
        return self.f 

    def stdin_array(self):
        self.arr=input().rstrip().split()
        return self.arr

    def stdin_integer_array(self):
        self.arr=list(map(int,input().rstrip().split()))
        return self.arr

def test(n,m,arr,brr):
        for i in range(n):
            i+=1
            crr=[]
            for j in range(m):
                if i%arr[j] == 0:
                    crr.append(brr[j])
            if crr == []:
                print(i)
            else:
                print(*crr)
                
def main():
    obj=StandardInput()
    arr,brr=[],[]
    n,m=obj.stdin_integer_array()
    for i in range(m):
        a,b=obj.stdin_array()
        arr.append(int(a))
        brr.append(b)
    test(n,m,arr,brr)

if __name__ == '__main__':
    main()
