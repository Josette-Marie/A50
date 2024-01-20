# Sum of even numbers in btw 10 and 30

sum = 0

for i in range(11, 30):
    if i%2 == 0:
        sum += i

print(f"Sum of even numbers in the interval > 10 to < 30 is : { sum}")