#Creted by Pooja
#On 14 June 2020
#Nested for loop imlementation using python
def threesquares(m):
   if m>=0:
       for p in range(0,m):
           for q in range(0,m):
               for r in range(0,m):
                   if p*p+q*q+r*r==m:
                       return(True)
       return(False)
   else:
       return(False)

x= threesquares(1000)
print(x)