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

def test(x, n):
    p=0
    for v in x.values():
        p+=min([v.count("L"), v.count("R")])
    return p
    
def main():
    obj=StandardInput()
    n=obj.stdin_integer()
    x={}
    for i in range(n):
        t,d=obj.stdin_array()
        if t in x.keys():
            x[t]=x[t]+d
        else:
            x[t]=d
    print(test(x, n))

if __name__ == '__main__':
    main()
