#write a program to find if the given number is prime no or not
#solution
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
num=int(input("Enter the number:"))
if prime(num):
    print("Its prime")
else:
    print("Its not a prime")