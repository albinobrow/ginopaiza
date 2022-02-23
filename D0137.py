#!/usr/bin/env python
# coding: utf-8

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

def test(s):
    count,n=0,len(s)
    for i in range(n):
        if s[i]=='y':
            count+=1
    return count

if __name__ == '__main__':
    obj=StandardInput()
    s=obj.stdin_string()
    print(test(s))
