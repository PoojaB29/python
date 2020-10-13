#Creted by Pooja
#On 13 Oct 2020
#dictionary manipulation using python

n=int(input("enter number of items "))
dict1={}
for i in range(n):

 key=input("enter the key ")
 value=input("enter it's value ")
 dict1[key]=value

print(dict1)
for key in sorted(dict1):
 print(" %s %s"%(key,dict1[key]))
print("enter dictionary 1 ")
d1={}
key=input("enter the key ")
value=input("enter it's value ")
d1[key]=value
print("enter dictionary 2 ")
d2={}
key=input("enter the key ")
value=input("enter it's value ")
d2[key]=value
d1.update(d2)
print(d1)
