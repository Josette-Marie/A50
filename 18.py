# prime numbers less than 100

for i in range(2, 100):
    count = 0
    for j in range(1, int(i/2) + 1):
        if i % j == 0:
            count += 1
    if count == 1:
        print(i, end=" ")        
