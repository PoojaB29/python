#Creted by Pooja
#On 13 Oct 2020
#Exception handling in python
import sys
randomList = ['a', 0, 2]
for entry in randomList:
    try:
   # do something
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except ValueError:
   # handle ValueError exception
       print(sys.exc_info()[0],"occured.")
       pass
    except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
       print(sys.exc_info()[0],"occured.")
       pass
    except:
   # handle all other exceptions
       print(sys.exc_info()[0],"occured.")
       pass
    finally:
       print("Code inside Final block ")
print("The reciprocal of",entry,"is",r)


        