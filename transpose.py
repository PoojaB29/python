#Creted by Pooja
#On 14 June 2020
#Implemented the transpose of matrix using python
def transpose(m):
    l=[]
    for i in range(len(m[0])):
        row=[]
        for j in m:
            row.append(j[i])
        l.append(row)
    return(l)
p=transpose([[1],[2],[3]])
print(p)       
            
