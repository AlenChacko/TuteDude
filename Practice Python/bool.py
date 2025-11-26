# 48. Simple comparison
a = 3.5
b = 6.7
print(a > b)
print(a < b)
print(a == b)

# 49. Between check
a = 10
b = 15
x = 13
if a > x > b:
    print(f"{x} is between {a} and {b}")
else:
    print(f"Not in between {a} and {b}")

# 50. All equal check
a = 10
b = 20
c = 30

if a == b == c:
    print("ALL EQUAL")
else:
    print("NOT EQUAL")

# 51. Leap year
# show me the answer

# 52. Logical operators
isStudent = True
isEmployed = False
isMarried = False

if isEmployed and isMarried and isStudent:
    print(True)
else:
    print(False)

#  53.Password check (simple)
password = "jsdgifger"
if password == "s3cr3t":
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")

# 54. Range of parity
n = 8
if n % 2 == 0 and n > 10 and n < 50:
    print(True)
else:
    print(False)

# 55. Comparison Chaining
print(1 < 2 < 3)
print(3 > 2 > 1)

# 56. Truthiness of values
text = ""
print(bool(text))  # False
txt2 = "sbd"
print(bool(txt2))  # True

# 57. Negation and double-negation
isStudent = False
print(not isStudent)
