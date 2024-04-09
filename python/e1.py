numbers = []

for n in range(1,1000):  
    
    if n%3 == 0 or n%5 == 0:
        numbers.append(n)
        sum_of_numbers = sum(numbers)
               
print(sum_of_numbers)
            
    
