import random
print("This program will print a combined list which contains odd numbers of 1st list and even numbers of 2nd list ")

list1 = []
list2 = []
list3 = []
for i in range(6):
    list1.append(random.randint(0, 100))
    list2.append(random.randint(0, 100))

for num in list1:
    if num % 2 != 0:
        list3.append(num)

for num in list2:
    if num % 2 == 0:
        list3.append(num)

print(list1)
print(list2)
print(list3)