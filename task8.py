import random
import math

mylist = [random.randint(20, 50) for _ in range(5)]
print(mylist)

even_numbers = [int(math.pow(i, 2)) for i in mylist if i % 2 == 0]
print(even_numbers)
