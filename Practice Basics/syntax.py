# 1. Hello, User!
name = input("Enter your name: ")
print("Hello", name)

# 2. Two-line output
print("Python\nRocks")

# 3. Comment and code
# single line comment
"""multi
line 
comment"""

# 4. Simple sum (read ints)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("Sum:", sum)

# 5. Echo with types
val = input("Enter someting: ")
print("Your entered", type(val), "type value")

# 6. Swap two variables
a = 10
b = 20
a, b = b, a
print("a:", a, "B:", b)

# 7.Multiple prints on one line
a = 1
b = 2
c = 3
print(f"a={a} b={b} c={c}")


# 8.Formatted output
name = "Alen"
age = 26
print(f"{name} is {age} years old")

# 9.Read & print floats
score = float(input("Enter a long float: "))
print(round(score, 2))

# 10. Input validation (int)
# show me the answer

# 11. Simple file-like output
print("*\n**\n***")
