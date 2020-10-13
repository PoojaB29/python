#Created by Pooja 
#On 22 Feb 2019
#This program is implemented for the addition and multiplication of polynomials using python
def addpoly(p1,p2):
    x = [0]*(max(p1[0][1],p2[0][1])+1)
    for i in p1+p2:
        x[i[1]]+=i[0]
    res =  [(x[i],i) for i in range(len(x)) if x[i]!=0]
    res.sort(key = lambda r: r[1], reverse= True)
    return res

def multpoly(p1,p2):
    x = [0]*(p1[0][1]*p2[0][1]+1)
    for i in p1:
        for j in p2:
            x[i[1]+j[1]]+=i[0]*j[0]
    res = [(x[i],i) for i in range(len(x)) if x[i]!=0]
    res.sort(key = lambda r: r[1], reverse= True)
    return res
a=addpoly([(2,1)],[(-2,1)])
print(a)
b=multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
print(b)
