import random
# our module
import pi_value

# between 1 and 10 included
random_integer = random.randint(1, 10)

# between 0 and 1 excluded by default
# *5 = range between 0 and 5 excluded (random.random() * 5)
random_float = random.random()

print(random_integer)
print(random_float)
print(pi_value.pi)
