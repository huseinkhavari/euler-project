def main(num):
    count = 0
    prime = 2
    while count < 10001:
        if div(prime):
            count += 1
        prime += 1
    return prime - 1

def div(x):
    prime = True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            prime = False
            break
    return prime

    
        
    

print(main(11000))

        