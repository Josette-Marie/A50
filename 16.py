# Return true if number is prime

def isPrime(num):
    count = 0
    limit =int(num /2)
    for i in range(1,limit + 1):
        if num % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False                                        
    
num = int(input("Enter a number : "))
print(f"Is If Prime : {isPrime(num)}")