num1 = 0
num2 = 1
num3 = 0
fibo_list = []
while num3 < 4000000:
    num3 = num1 + num2
    if num3 < 4000000:
        fibo_list.append(num3)
    num1 = num2
    num2 = num3

evens_fibo = [num for num in fibo_list if num % 2 == 0]
print(sum(evens_fibo))
