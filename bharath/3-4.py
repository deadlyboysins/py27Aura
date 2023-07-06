def prime(n):
    a=0
    for i in range(2,n):
        t=n%i
        if(t ==0):
            a=1
    if(a==1):
        print("not prime")
    else:
        print("prime")
prime(5)


def prime(n):
    a=0
    i=2
    while(i<n):
        t=n%i
        if(t ==0):
            a=1
        i +=1
    if(a==1):
        print("not prime")
    else:
        print("prime")
prime(4)