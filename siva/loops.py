#2.1
i=0
n=7
while(i <= n-1):
    print(i)
    i+=1
print(i-1)

#2.2
i=0
n=7
while(i <= n-1):
    print(i)
    i+=1
print(i-1)

#2.3
i=0
n=7
for i in range(0,n+1):
    print(i)
    i +=1
print(i)

#2.4
n=7
for i in range(0,n):
    print(i)
    i += 1
print(i)

#2.5
i=0
n=5
while(5<n):
    print(i)
print(i)

#2.6
n=5
i=-3
while(i<n):
    print(i)
    i +=1
print(i)

#2.7
i=0
n=5
for i in range(0,n):
    print(i)
    i +=1
print(i)

#2.8
i=0
n=10
while(i<n):
    print(i)
    if(i == 5):
        break
    i +=1
print(i)

#2.9
i=1
n=10
while(i<=n):
    print(i)
    i +=2
print(i-2)


#2.10
i=0
n=5
for i in range(1,n+1):
    print(i)
    if(i==5):
        i+=5
        print(i)
    i+=5
print(i)

2.11
i=0
n=6
x=2
for i in range(1,n):
    for j in range(1,n):
        print(i,j)
    i+=1
    j+=1
print(i,j)


#2.12
i=0
n=6
x=2
for i in range(1,n):
    print(i,end="")
    for j in range(1,n):
        print(j,end="")
    print("")
    i+=1
    j+=1
print(i,j)