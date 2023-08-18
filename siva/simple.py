#1.1
a = 426
c = 0
c = c + a % 10
a = int(a/10)

c = c + a % 10
a = int(a/10)

c = c + a % 10
a = int(a/10)

print("sum c :" ,c)


#1.2
a = 426
c = 0

c = (c*10) + (a%10)
a = int(a/10)
c = (c*10) + (a%10)
a = int(a/10)
c = (c*10) + (a%10)
a = int(a/10)
print(c)

#1.3
num = 626
temp = num
rev = 0

for i in range(len(str(num))):
    rev = rev * 10 + num % 10
    num = num // 10

if temp == rev:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")




#1.5 promoted or not

"""independent if method"""


s1=90; s2=50; s3=60
t = 0
if(s1>=35):
    t=t+1
if(s2>=35):
    t=t+1
if(s3>=35):
    t=t+1
if(t==3):
    print("prompted")
else:
    print("not prompted")





"""Nested if method"""


s1=65; s2=20; s3=80
x = 0
if(s1>=35):
    if(s2>=35):
        if(s3>=35):
            x = 1
if(x == 1):
    print("promoted")
else:
    print("Not promoted")
