#Creted by Pooja
#On 12 March 2020
#Remove duplicates from the list using python
def removedup(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    return (l1)
        
       
b=removedup([3,5,7,5,3,7,10])
print(b)
