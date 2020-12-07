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

def test(arr):
    ans=[]
    for i in arr:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
            ans.append(i)
    return ''.join(ans)

if __name__ == '__main__':
    obj=StandardInput()
    arr=list(obj.stdin_string())
    print(test(arr))
