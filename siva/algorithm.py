#4.1 Write a program which replaces all duplicate elements with '0' in a single dimensional integer array.

a = [2,4,2,6,4,7,5]
n = 7
x = 1
for i in range(0,n-1):
    print(i,end = " ")
    for j in range(x,n):
        print(j,end = " ")
    x = x+1
    print()
print(a)
n = 7
x = 1
for i in range(0,n-1):
    for j in range(x,n):
        if (a[i] == a[j]):
            print(a[j], "Is duplicate")
            a[j] = 0
    x = x+1
print(a)

#4.2 Write a program to remove all duplicate elements in a single dimensional integer array.?

a = [2,4,2,6,4,7,5]

print(a)
i = 0
n = 7
x = 1
j = 1
while(i< n-1):
    j = x
    while(j<n):
        if(a[i] == a[j]):
            print(a[j], "Is duplicate")
            del (a[j])
            n = n - 1
        j = j + 1
    i = i+1
    x = x+1

print(a)


#4.3 write a program to sort 'n' integer values in a single dimensional array

a =[1,3,5,8,2,4]

print(a)
n = len(a)
x = 1
for i in range(0,n-1):
    for j in range(x,n):
        print(i,j)
        if(a[i] < a[j]):
            t = a[i]
            a[i] = a[j]
            a[j] = t
    x= x + 1
print(a)


#4.4 Addition of two matrices


row = 3
col = 3


a =[[2,5,6],
    [1,8,4],
    [3,7,0]]

b = [[8,7,1],
    [1,3,2],
    [0,2,0]]

c =[[0,0,0],
    [0,0,0],
    [0,0,0]]

print(a)
for i in range(0,row):
    for j in range(0,col):
        print(a[i][j], end=" ")
    print()

print(b)
for i in range(0,row):
    for j in range(0,col):
        print(b[i][j], end=" ")
    print()

print(c)
for i in range(0,row):
    for j in range(0,col):
        print(c[i][j], end=" ")
    print()

for i in range(0,row):
    for j in range(0,col):
        c[i][j] = a[i][j] + b[i][j]
    print( )

print(c)
for i in range(0,row):
    for j in range(0,col):
        print(c[i][j], end=" ")
    print()



#4.5 Multiplication of matrix


a =   [[12, 7, 3],
      [4, 5, 6],
      [7, 8, 9]]

b = [[1, 5, 6, 7],
    [4, 6, 9, 5],
    [8, 4, 3, 6]]

result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

for i in range(0,3):
    for j in range(0,4):
        for k in range(0,3):
            result[i][j]+= a[i][k]*b[k][j]
for r in result:
    print(r)
