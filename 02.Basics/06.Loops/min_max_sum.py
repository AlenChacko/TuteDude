scores = [2, 3, 65, 33, 88, 44, 32, 75, 23, 54, 23, 65, 12, 86]

# sum
total = 0
for score in scores:
    total += score

print(f"Total = {total}")


# highest
highest = scores[0]
for score in scores:
    if highest < score:
        highest = score
print(f"Highest = {highest}")


# lowest
lowest = scores[0]
for score in scores:
    if lowest > score:
        lowest = score
print(f"Lowest = {lowest}")


print(f"Highest score = {max(scores)}")
print(f"Lowest score = {min(scores)}")
print(f"Total score = {sum(scores)}")
