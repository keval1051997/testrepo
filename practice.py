"""def fact(n):
    factorial = 1
    for x in range(1,n+1):
        factorial = factorial * x
    print(factorial)

fact(11)

Recursive Function:

def fact(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * fact(n-1)

print(fact(8))

Fibonacci numbers

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)
print(fib(4))

**Square of numbers 1 to 10

squares = [value**2 for value in range(1,11)]
print(squares)

** One Million:

million = list(range(1,1000001))

print(min(million))
print(max(million))
print(sum(million))

**ODD number:

odd_numbers = list(range(1,20,2))

for i in odd_numbers:
    print(i)

**THREE:

multiples = list(range(3,31,3))

for i in multiples:
    print(i)

**CUBES:

cubes = [value**3 for value in range(1,11)]
print(cubes)

for i in range(1,11):
    value = i**3
    cubes.append(value)
print(cubes)

**Slicing


my_pizza = ['jalapeno_onion', 'pepproni', 'mushroom']

my_friends_pizza = my_pizza[:]

my_pizza.append('jalapeno_greenpaper')
my_friends_pizza.append('onion_mushroom')

print("my favorite pizzas are: ")

for i in my_pizza:
    print(i.title())

print("\nMy friend's favorite pizzas are: ")

for i in my_friends_pizza:
    print(i.title())

** Understanding Tuples

buffett = ('roti', 'sabji', 'daal', 'chawal')

print('Original buffett: ')

for i in buffett:
    print(i)

buffett = ('rotlo', 'sabji', 'kadhi', 'chawal')

print('\nRevised buffett: ')

for i in buffett:
    print(i)

**IF boolean:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
"""


import random

n = 3  

if n%2 != 0:
    print("Weird")
elif n in range(2,5) and n%2==0:
    print("Not Weird")
elif n%2==0 and n in range(6,21):
    print("Weird")
elif n%2==0 and n>20:
    print("Not Weird")








