# nth fib of a number using recusion 

def Fib(num):
    if num <= 1:
        return num
    
    return Fib(num - 1) + Fib(num - 2)

num = int(input("Enter the number of terms: "))
print(f"Fib({ num }) = {Fib(num)}")