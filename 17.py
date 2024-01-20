# Sum of numbers of digits of a positive number

sum = 0
count = 0 
num = int(input("Enter a number : "))

if num < 0:
    print("Only for positive integers")

while num != 0:
    digit = num%10
    sum += digit
    num /= 10
    

print(int(sum))
