import sys

print("New warnings are introduced in current build, can't be promoted")

#file open 1
x = open(sys.argv[1], "rt")
data = x.read()
# reading the word warnings
a=  data.count("warning")
x.close()

#file open 2
y = open(sys.argv[2], "rt")
data = y.read()
# reading the word warnings
b=  data.count("warning")
y.close()

print(f"old warning count{sys.argv[1]}:",a)
print(f"new warning count{sys.argv[2]}:",b)

if (a>b):
    print("build can be promoted")
else:
    print("build cannot be promoted")
