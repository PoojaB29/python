#Creted by Pooja
#On 14 June 2020
#rank of student as per the marks
N=int (input())
M=[]
for i in range(N):
    a=int(input())
    M.append(a)
M.sort(reverse=True)
S=int(input())
for i in range(len(M)):
    if M[i]==S:
        print(i+1)
