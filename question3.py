#write a program to find the factorial of a number
#solution
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
num=int(input("Enter the number:"))
print(fac(num))