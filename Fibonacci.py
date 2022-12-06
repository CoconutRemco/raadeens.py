# Python program to display the Fibonacci sequence

import random
from statistics import variance


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = random.randint(32,33)
fibonaci = []
# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
       fibonaci.append(recur_fibo(i))
fibonaci.reverse()
var1 = fibonaci[0:1]
var2 = fibonaci[1:2]
integers = [1, 2, 3]
strings = [str(integer) for integer in var1]
a_string = "". join(strings)
variabele1 = int(a_string)
integers = [1, 2, 3]
strings = [str(integer) for integer in var2]
a_string = "". join(strings)
variabele2 = int(a_string)
print(variabele1+variabele2/variabele1)


