# Banker Roulette
# Who will pay the bill?

# Figure out how to pick a random name from the list of friends.

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]


random_friend = random.choice(friends)
print(random_friend)
# or 

print(random.choice(friends))

# or

random.index = random.randint(0, 4)
print(friends[random.index])

# or

print(friends[random.randint(0, len(friends) - 1)])

