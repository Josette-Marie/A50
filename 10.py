# Sum of n elements in an array

Numbers = []

sum = 0
i = 0

length = int(input("Enter the length of the arrary : "))

while i != length:
    num = int(input("Enter a number : "))
    Numbers.append(num)
    sum += Numbers[i]
    i+=1

print(Numbers)
print(f"Sum = { sum }")