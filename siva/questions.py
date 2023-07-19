
#Tuple questions
#question No:1
#Q)Get index of minimum value..?

'''
tA = (123, 283)
min_index = tA.index(min(tA))

print(min_index)

# o which indicates that the minimum value ("123") is located at index '0' in the tuple
'''

#question No:2
# Q) What happens to max() and min() if tuple consists int and strings..?

'''
tA = (123,'abc', 283)
maximum = max(tA)
minimum = min(tA)

print(maximum)
print(minimum)
'''
#Type error : Not supported between instances of 'str' and 'int'


#question NO:3
#Is list hass max() and min()..?
'''
tA = (123, 283)
my_list = list(tA)
maximum = max(my_list)
minimum = min(my_list)

print(maximum)
print(minimum)

'''

#question No:4
#Q) Add a string '823' to tuple..?

tB = (345, 'abb')
tC = tB + tuple("823")

print(tC)
