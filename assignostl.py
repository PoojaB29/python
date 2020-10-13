#Creted by Pooja
#On 13 Oct 2020
#The program is implemented to learn elif statement.

def fizz_buzz(a):
    if a%3==0 and a%5==0:
        return("FizzBuzz")
    elif a%5==0:
        return("Buzz")
    elif a%3==0:
        return("Fuzz")
    else:
        return(a)

a=int(input())
print(fizz_buzz(a))

