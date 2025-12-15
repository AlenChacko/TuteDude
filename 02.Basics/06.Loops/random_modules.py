import random

# random() -> returnes a radom float between 0.0 and 1.0, (1.0 excluded)
print(random.random())

# randint(a,b) -> returnes random integer between a and b
print(random.randint(10, 20))

# choice(sequence) -> returns a random item from the sequence
my_list = ["Alen", 26, "Cherupuzha", True]
print(random.choice(my_list))

# shuffle(sequence) -> returns elements shuffled in random order
random.shuffle(my_list)
print(my_list)
