#Creted by Pooja
#On 5 March 2020
def hillvalley(l):
    a=0
    d=0
    if l[0]<l[1]:
        for i in range(1,len(l)):
            if l[i-1]<l[i]:
                a=a+1
        for i in range(a,len(l)-1):
            if(l[i]>l[i+1]):
                d=d+1
        if(a>0 and d>0 and a+d==len(l)):
            return(True)
        else:
            return(False)
    else:
        for i in range(1,len(l)):
            if l[i-1]>l[i]:
                d=d+1
        for i in range(d,len(l)-1):
            if(l[i]<l[i+1]):
                a=a+1
        if(a>0 and d>0):
            return(True)
        else:
            return(False) 
x=hillvalley([1,2,3,4,5,3,2,4,5,3,2,1])
print(x)  