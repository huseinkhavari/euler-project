from sympy import factorint

number = 600851475143

prime_factors = factorint(number).keys()

print(max(prime_factors))

    


