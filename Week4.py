#Creted by Pooja
#On 5 March 2020
#Implementation of merge-sort and quicksort using python.
# Week 4
def merge(A,B):
    (C,m,n)=([],len(A),len(B))
    (i,j)=(0,0)
    while i+j<m+n:
        if i==m:
            C.append(B[j])
            j=j+1
        elif j==n:
            C.append(A[i])
            i=i+1
        elif A[i]<=B[j]:
            C.append(A[i])
            i=i+1
        elif A[i]>B[j]:
            C.append(B[j])
            j=j+1
    return(C)
def mergesort(A,l,r):
    if r-l<=1:
        return(A[l:r])
    if r-l>1:
        mid=l+r//2
        L=mergesort(A,l,mid)
        R=mergesort(A,mid,r)
    return(merge(L,R))
def quicksort(A,l,r):
    if l-r<=1:
        return()
    yellow=l+1
    for green in range(l+1,r):
        if A[green]<=A[l]:
            (A[yellow],A[green])=(A[green],A[yellow])
            yellow=yellow+1
    (A[l],A[yellow-1])=(A[yellow-1],A[l])
    quicksort(A,l,yellow-1)
    quicksort(A,yellow,r)
        
