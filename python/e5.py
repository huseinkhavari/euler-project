def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)


lcm_of_numbers = 1
for i in range(1, 21):
    lcm_of_numbers = lcm(lcm_of_numbers, i)

smallest_number = lcm_of_numbers
while smallest_number < 252000:
    smallest_number += lcm_of_numbers

print(smallest_number)