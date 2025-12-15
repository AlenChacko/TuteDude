# * * * * *
for i in range(6):
    print("*", end=" ")

# *
# *
# *
# *
# *
for i in range(6):
    print("*")


# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()


# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

for i in range(1, 5):
    for j in range(1, 5):
        print(j, end=" ")
    print()


# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(6):
    for j in range(i):
        print("*", end=" ")
    print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1, 6):
    for j in range(i):
        print(j + 1, end=" ")
    print()


# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()


# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
