#Creted by Pooja
#On 8 March 2020
#sample program using python
x= int(input ("enter no:"))
n=int(input ("enter no of inputs :"))
sum=0
for i in range(1,n+1):
    sum=sum+((x**i)/i**i)
for i in range(1,n):
    print("{}**{}/{}**{}+".format(x,i,i,i),end="")
#i=i+1
print("{}**{}/{}**{}={}".format(x,i+1,i,i,sum))
m=int(input())
for i in range(1,m+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print("\n")
for i in range(m-1,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print("\n")