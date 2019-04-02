#!/usr/bin/python
import sys

def get_list_fasta(lid,fasta):
    f=open(fasta)
    c=0
    for line in f:
        line=line.rstrip()
        if line[0]=='>':
            tid=line.split('|')[1]
        if tid in lid:
            c=1
        else:
            c=0
        if c==1 :
            print(line)


if __name__=="__main__":
    fid=sys.argv[1]
    fasta= sys.argv[2]
    lid=open(fid).read().split('\n')
    get_list_fasta(lid,fasta)
