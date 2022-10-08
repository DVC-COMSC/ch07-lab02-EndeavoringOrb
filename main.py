import random

numbers = []
for i in range(10):
    numbers.append(random.randint(0,100))
print(numbers)
print(min(numbers),numbers.index(min(numbers)))
