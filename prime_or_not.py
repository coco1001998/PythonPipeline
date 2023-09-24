def primeOrNot(param):
    for i in range(2, param):
        if((param%i)==0):
            print(param, "is a prime number")
            break

num=int(input("Please enter the number:"))

if num > 1:
    primeOrNot(num)
else:
    print("Enter a valid number!")