#write a program to find the sum of digits of a given number'
#solution
sum=0
num=int(input("Enter the number:"))
while(num):
    rem=num%10
    sum+=rem
    num//=10
print(sum)