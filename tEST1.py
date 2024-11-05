num = int(input("Enter the number :"))
new_list = []
for x in range(2,num):
    for i in range(2,int(x/2)+1):
        if x%i==0:
            print(f"{x} is not prime number")
            break
    else:
        print(f"{x} is a prime number")
        new_list.append(x)
print(new_list)
print(int(1.5))
