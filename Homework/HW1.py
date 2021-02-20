prime_numbers = []

for number in range(1,100+1):
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                break
        else:
            prime_numbers.append(number)


prime_numbers_matrix = []  
prime_numbers_element = []

for number in prime_numbers[::-2]:
    prime_numbers_element.append(number)            
    if len(prime_numbers_element) == 3:
        prime_numbers_matrix.append(prime_numbers_element)
        prime_numbers_element = []
    elif len(prime_numbers_matrix) == 3:
        break    


print(prime_numbers_matrix)