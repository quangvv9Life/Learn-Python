a = ["banana" , "apple" , "microsoft"]
# print(a[0])
# print(a[1])
# print(a[2])

# replacement of above manual methods by using for loops

for data in a:
    print(data)

b = [20, 10, 5]
total = 0
for element in b: #this word 'element' can be chosen by any words
    total = total + element
print(total)

range(1, 5) # create a range of numbers starting from 1 to 5 but not including 5
c = list(range(1, 5)) #list() use to convert range into list
print(c)

total2 = 0
for i in range(1, 5):
    total2 += i #increment by i value = total2 + i
print(total2)


#modular operator:
print(4 % 3) #get the remainder of division
list(range(1, 8 ))
total3 = 0
for i in range(1, 8):
    if i % 3 == 0:
        total3 += i
print(total3)