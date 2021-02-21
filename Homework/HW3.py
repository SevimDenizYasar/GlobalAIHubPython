primeFirst = []
primeSecond = []

def prime_first(number):
    primeFirst.append(number)
    
def prime_second(number):
    primeSecond.append(number)
    
def primeness(number):
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                break
        else:
            return True

for i in range(0,1000+1):
    if i <= 500 and primeness(i):
        prime_first(i)
    elif i>= 500 and primeness(i):
        prime_second(i) 
   
print("Prime Numbers between 0-500 are:",primeFirst)
print("Prime Numbers Between 500-1000 are:",primeSecond)
 
          
