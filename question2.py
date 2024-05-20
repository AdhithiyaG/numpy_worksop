# find if the given number is a palindrome or not?
# solution
num=int(input("Enter the number:"))
num_str=str(num)
if num_str==num_str[::-1]:
    print("Its palindrome")
else:
    print("Its not palindrome")