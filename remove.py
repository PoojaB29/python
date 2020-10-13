#Creted by Pooja
#On 12 March 2020
#Remove the same numbers from the list
def remdup(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    return (l1)
        
       
b=remdup([3,5,7,5,3,7,10])
print(b)