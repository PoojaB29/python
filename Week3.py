#Creted by Pooja
#On 5 March 2020
#Implementation of sorting algorithms using python.
#Week 3
def findpos(l,v):
    (found,i)=(False,0)
    while i<len(l):
        if not found and l[i]==v:
            (found,pos)=(True,i)
    if not found:
        pos=-1
    return(pos)
def search(seq,v):
    for x in seq:
        if x==v:
            return(True)
    return(False)
def binarysearch(seq,v,l,r):
    if (r-l==0):
        return(False)
    mid=(l+r)//2
    if v==seq[mid]:
        return(True)
    if v<seq[mid]:
        return(binarysearch(seq,v,l,mid))
    else:
        return(binarysearch(seq,v,mid+1,r))
def seletionsort(l):
    for start in range(len(l)):
        minpos=start
        for i in range(start,len(l)):
            if l[i]<l[minpos]:
                minpos=i
                (l[start],l[minpos])=(l[minpos],l[start])
def insertionsort(seq):
    for sliceend in range(len(seq)):
        pos=sliceend
        while pos>0 and seq[pos]<seq[pos-1]:
            (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos])
            pos=pos-1