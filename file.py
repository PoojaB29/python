#Creted by Pooja
#On 13 Oct 2020
#File manipulation using python

f1 = open("test.txt", "w") 
str1 = input("Enter a string: ") 
f1.write(str1) 
f1.close() 
f1 = open("test.txt", "r") 
l = 0 
c = 0 
w = 0 
for i in f1: 
    l = l + 1 
    L = i.split(" ") 
    w = w + len(L) 
    c = c + len(i) - w
f1.seek(0, 0) 
str2 = f1.read() 
print("Number of line: ", l) 
print("Number of words:", w) 
print("Number of characters: ", c) 
f2 = open("F2.txt", "w") 
#print(f2.read())
f2.write(str2) 
f1.close() 
f2.close()

