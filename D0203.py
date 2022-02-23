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

def test(s,c,n):
    if s[n-1] == c:
      return "Yes"
    else:
      return "No"

def main():
    obj=StandardInput()
    s=obj.stdin_string()
    c=obj.stdin_string()
    n=obj.stdin_integer()
    print(test(s,c,n))

if __name__ == '__main__':
    main()
