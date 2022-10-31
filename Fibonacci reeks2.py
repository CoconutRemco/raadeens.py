import random


def berekenfibonacci(n):
   if n <= 1:
       return n
   else:
       return(berekenfibonacci(n-1) + berekenfibonacci(n-2))

nterms = random.randint(4,30)


if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(berekenfibonacci(i))