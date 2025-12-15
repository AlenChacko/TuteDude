# break and exit loop when a condition met
for i in range(1, 11):
    print(i)
    if i == 5:
        break

# skip the current iteration when condition met
for i in range(1, 11):
    print(i)
    if i == 5:
        continue
