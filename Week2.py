#Created by Pooja
#On 3 june 2020
#Implemented divide, even, odd, factors, factorial, isprime, primeupto,  nprime function using python
#WEEK 2
def divides(m,n):
    if n%m==0:
        return(True)
    else:
        return(False)
def even(n):
    return(divides(2,n))
def odd(n):
    return(not divides(2,n))

def factors(n):
    flist=[]
    for i in range(1,n+1):
        if n%i==0:
            flist=flist + [i]
    return(flist)

def factorial(n):
    if n<=0:
        return(1)
    else:
        val=n*factorial(n-1)
        return(val)

def isprime(n):
    return(factors(n)==[1,n])#Ans is bool when called

def primeupto(n):
    plist=[]
    for i in range(1,n+1):
        if isprime(i):
            plist=plist+[i]
    return(plist)

def nprime(n):
    (count,i,plist)=(0,1,[])
    while(count<n):
        if isprime(i):
            (count,plist)=(count+1,plist+[i])
        i=i+1
    return(plist)