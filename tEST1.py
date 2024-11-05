import math
#num = int(input("Enter the number :"))
new_list = [1,2,3,2,3,2,4,3,5,2,5]
lis = []
for x in new_list:
    if x not in lis:
        lis.append(x)
        print(f"{x} is found  {new_list.count(x)} times")




