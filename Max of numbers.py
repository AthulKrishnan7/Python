number = int(input("Enter number numbers of input = "))

count =0
n = int(input("Enter the number :"))
max = n
while count < number - 1 :
    n = int(input("Enter the number :"))
    count= count+1
    if n > max :
        max =n
print(max)
