import random
n = random.randint(1,1000)
guess = 0
while guess!=n :
    guess = int(input("Enter your guess 😁 : "))
    if guess > n :
        print("The number is smaller")
    elif guess <n :
        print("The number is greater")
    else :
        print("YES, The number is ",guess)