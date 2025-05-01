#Merge two lists using the following condition
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
result_list = []

for x in list1:
    if x % 2 != 0:
       result_list.append(x)
for i in list2:
    if i % 2 == 0:
        result_list.append(i)

print(result_list)



























































