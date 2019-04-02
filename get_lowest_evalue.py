#!/usr/bin/python
import sys
from math import inf

def get_lowest(filename):
    d={}
    f=open(filename)
    for line in f:
        v=line,split()
        sid=v[0]
        eva=float(v[10])
        d[sid]=min(d.get(sid,maxv), eva)
    return d



if __name__== '__main__':
    filename=sys.argv[1]
    d=get_lowest(filename)
    for k in d.keys():
        print k,d[k]

