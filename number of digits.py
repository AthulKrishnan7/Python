num = int(input("Enter the number :"))
number = num
count = 0
while num > 0:
    rem = num / 10
    num = num // 10
    print(rem, num)
    count = count + 1
print("Number of digits in ", number, " is ", count)
