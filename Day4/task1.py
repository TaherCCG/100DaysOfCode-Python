# Random Module
import random

print("Random number:")
random_integer = random.randint(1, 10)
print(random_integer)

print("Random.random number:")
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

print("Random float:")
random_float = random.uniform(1, 10)
print(random_float)

print("Random heads or tails:")
random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

