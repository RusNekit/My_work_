numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
num = len(numbers)
for i in range(2, num+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        primes.append(j)
    else:
        not_primes.append(j)
print(primes)
print(not_primes)
