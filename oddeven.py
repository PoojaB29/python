#Creted by Pooja
#On 20 Feb 2020
#Implemented program to sum the squares of the numbers in the list
def sumsquare(l):
    sum=0
    diff=0
    l1=[]
    for i in l:
        if i%2==0:
            sum=sum+(i*i)
        else:
            diff=diff+(i*i)
    l1.append(diff)
    l1.append(sum)
    return(l1)
p=sumsquare([1,3,5])
print(p)
        
