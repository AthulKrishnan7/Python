import math
#num = int(input("Enter the number :"))
new_list = [1,2,3,2,3,2,4,3,5,2,5,7]
even_lis = []
odd_lis = []
for x in new_list:
    if x%2 ==0:
        even_lis.append(x)
    else:
        odd_lis.append(x)
print(f' Sum of odd numbers of list {sum(odd_lis)}')
print(f' Sum of odd numbers of list {sum(even_lis)}')



