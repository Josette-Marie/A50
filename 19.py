# Returnig the prime number greater than the array size

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
    

def CheckPrime(array,n):
    array2 = []
    for i in range(len(array)):
        if isPrime(array[i]) == True:
            if array[i] > n:
                array2.append(array[i])
    return array2

array = [2,3,6,7]
n = len(array)
print(CheckPrime(array,n))

    