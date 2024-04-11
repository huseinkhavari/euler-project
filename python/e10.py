def prime(number):
    primes = [2]
    for num in range(3, number, 2):
        for x in primes:
            if num % x == 0:
                break
            elif num < x*x:
                primes.append(num)
                break

    return sum(primes)

print(prime(2000000))
