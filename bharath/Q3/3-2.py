def factorial(n):
    f = 1
    for i in range(1,n+1):
        f= f*i
    return f
a=factorial(5)
print(a)

def factorial(n):
    f = 1
    i=1
    while(i<=n):
        f = f*i
        i +=1
    return f
a=factorial(5)
print(a)
