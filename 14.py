n_term = 10
num1,num2 = 0,1
count = 0


print(f"Fib({n_term})")

while count < n_term:
    print(num1, end=", ")
    nth = num1 + num2
    num1 = num2
    num2 = nth
    count += 1
