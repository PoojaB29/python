#Creted by Pooja
#On 5 March 2020
#The program contains the different ways to implement gcd function using python.
def gcd(m,n):
    fm=[]
    for i in range(1,m+1):
        if(m%i)==0:
            fm.append(i)
    fn=[]
    for j in range(1,n+1):
        if (n%j)==0:
            fn.append(j)
    cf=[]
    for f in fm:
        if f in fn:
            cf.append(f)
    return(cf[-1])

def gcd1(m,n):
    cf=[]
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            cf.append(i)
    return(cf[-1])

def gcd2(m,n):
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            mrcf=i
    return(mrcf)
#backward scanning
def gcd3(m,n):
    i=min(m,n)
    while i>0:
        if m%i==0 and n%i==0:
            return(i)
        else:
            i=i-1

#Euclids Algorithm
def gcd4(m,n):
    #Assume m>=n
    if m<n:
        (m,n)=(n,m)
    if (m%n)==0:
        return(n)
    else:
        diff=m-n
        return(gcd(max(n,diff),min(n,diff)))

def gcd5(m,n):
    if m<n: #Assume m>=n
        (m,n)=(n,m)
    while m%n!=0:
        diff=m-n
        (m,n)=(max(n,diff),min(n,diff))
    return (n)
 
def gcd6(m,n):
    if m<n:
        (m,n)=(n,m)
    if (m%n)==0:
        return (n)
    else:
        return(gcd(n,m%n))#m%n<n always as remainder is always less than divisor

def gcd7(m,n):
    if m<n:
        (m,n)=(n,m)
    while m%n!=0:
        (m,n)=(n,m%n)
    return (n)
