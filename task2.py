# Simple Calculator
def add(a, b):
    return a + b

def sub(a, b):
    if a>b:
        return(a-b)
    else:
        return(b-a)
    
def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b
print('Welcome to calculator')
a = float(input('Enter first number: '))
b = float(input('Enter second number: '))

print('What do you want to perform?')
print('1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Modulus')
c = int(input())

if c == 1:
    print('Addition =', add(a, b))
elif c == 2:
    print('Subtraction =', sub(a, b))
elif c == 3:
    print('Multiplication =', mul(a, b))
elif c == 4:
    print('Division =', div(a, b))
elif c == 5:
    print('Modulus =', mod(a, b))
else:
    print('Invalid input')
