# 71. Predict output
x = 5
print("x =", x)
x = x + 2
print(x)

# 7 will be the output

# 72. Find the bug: type error
a = "5"
b = 3
# print(a + b)

# TypeError because a string type cannot add a number type value with it

# 73. Logic bug
# n = int(input())
# if n % 2:
#     print("EVEN")
# else:
#     print("ODD")

# To check the even number the if condition should be like n%2==0

# 74. Off-by-one
n=8
print(list(range(1,n)))
print(list(range(1,n+1)))
# The n+1 method prints the correct value because the python range function is always exclusive of the stop value

# 75. Wrong variable name
name = input()
# print(Nmae) # not defined error
print(name) #corrected version

# 76. Prediction: float formatting
# print("{:.2f}".format(2.3456))
# print(round(2.3456, 2))

#show me the answer

# 77. Debug an input conversion
x = input("Enter a number: ")
print(x * 2) # this will print the number 2 times
# the correct way is to add int(input("Enter a number"))
# or
# int(x)
print(int(x)*2)


# 78. String immutability
s="abc"
# s[0] = "z" Type error string character do not allow reassignment
#  show me how to create the string "zbc"

# 79. NameError from missing input
ready="True"
if ready:
    print("Go!")

# ready isn't defined in the code

# 80. Predict output: chained assignment
a = b = c = 10
a += 5
print(a, b, c)

# 15,10,10

