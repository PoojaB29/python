#Creted by Pooja
#On 13 Oct 2020
#Numbers manipulation using  python

l=[]
n= int(input('Enter no. of elements'))
print('enter elements')
for i in range (0,n):
 l.append(int(input()))
print(l)
odd=[]
even=[]
for i in range (n):
 if(l[i]%2==0):
     even.append(l[i])
 else:
     odd.append(l[i])
print("1.Seperate elements\n2.Merge and Sort\n3.Update first element\n4.Print middle elment")
ch=int(input('Enter Choice '))
if(ch==1):
 print(l,odd,even)
elif(ch==2):
    fin=[]
    fin=odd+even
    print(fin)
    fin.sort()
    print(fin)
elif(ch==3):
 l[0]=int(input('Enter new value'))
 print(l)
elif(ch==4):
 k=int(len(l)/2)
 print(l[k])
else:
 print("Invalid input")