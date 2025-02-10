'''
What is random.seed()?

When generating random numbers in Python using functions like random.random() or randint(),

the results are typically unpredictable.

However, by using seed initialization, we can ensure that the same sequence of random numbers 

is generated each time our program runs.
'''
import random
random.seed(10)
print(random.random())