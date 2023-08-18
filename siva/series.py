#3.1

#sum  of n terms of Fibonacci series?
n = 5

a = 0
b = 1 
for i in range(n):
    print(a)
    temp = a
    a = b
    b = temp + b



#3.2 factorial value of n


def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    print(f)

a = 5
factorial(a)


#3.3 How to check whether given number 'n' is prime or not?

def is_prime():
    n = 22
    fc = 0
    for i in range(1,n+1):
        rem = n%i
        if(rem == 0):
            fc = fc + 1
    if (fc > 2):
        print(n,  "Not a prime")
    else:
        print(n, "prime")
is_prime()



#3.4
def is_prime(n):
    fc = 0
    for i in range(1,n+1):
        rem = n%i
        if(rem == 0):
            fc = fc + 1
            
    if (fc > 2):
        return 0
    else:
        return n

n = 15
for i in range(1, n+1):
    retval = is_prime(i)
    if(retval == i):
        print(i)



#3.5

def is_prime(n):
    fc = 0
    for i in range(1,n+1):
        rem = n%i
        if(rem == 0):
            fc = fc + 1
            
    if (fc > 2):
        return 0
    else:
        return n
n = 10
s = 0
for i in range(1,n+1):
    retval = is_prime(i)
    if(retval == i):
        s = s + i
print(s)


#3.6

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

n = 5
for i in range(1,n+1):
    print(factorial(i))


#3.7

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

n = 5
s = 0
for i in range(1,n+1):
    s = s+factorial(i)
print(s)



#3.8

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

n = 5
s = 0
for i in range(1,n+1):
    nfv = factorial(i+1)
    dfv = factorial(i)
    s = s + nfv /dfv

print(s)



#3.9

for i in range(1,6):
    print(i, end= " ")
for i in range(4, 0, -1):
    print(i, end= " ")

#3.10
n = 5
x = n + 1
for i in range(1, n+1):
    for j in range(1,x):
        print(j,end=" ")
    x = x -1
    print()

#3.11

n = 5
x = n+1
for i in range(1, n+1):
    for j in range(1,x):
        print(j,end =" ")
    x = x-1
    print()
    
#3.12

n = 5
x = 2
for i in range(1,n+1):
    for j in range(1,x):
        print(j,end=" ")
    x = x+1
    print()

#3.13

n = 5
x = 2
for i in range(n):
    for j in range(n-i-1):
        print(" ",end =" ")
    for j in range(i+1):
        print(j+1,end=" ")
    x = x+1
    print()