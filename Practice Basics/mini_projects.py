# 81. Simple calculator


num1 = int(input("Enter first input: "))
operator = input("Enter operator input: ")
num2 = int(input("Enter second input: "))

if operator == "+":
    print(f"{num1}+{num2}={num1+num2}")
elif operator == "-":
    print(f"{num1}-{num2}={num1-num2}")
elif operator == "*":
    print(f"{num1}*{num2}={num1*num2}")
elif operator == "/" and num2 == 0:
    print("Cannot divide by Zero")
elif operator == "/":
    print(f"{num1}/{num2}={num1/num2}")
else:
    print("Invalid operator")


# 82. Grade calculator
marks=int(input("Enter your mark: "))
if marks >= 90 and marks <= 100:
    print("You got A Grade")
elif marks >= 75:
    print("You got B Grade")
elif marks >= 60:
    print("You got C Grade")
elif marks >= 40:
    print("You got D Grade")
elif marks < 40:
    print("You got F Grade")
else:
    print("Invalid input")


# 83. Temperature classifier
cel = float(input("Enter temparature in celsius: "))
if cel <= 10:
    print("Cold")
elif cel > 10 and cel <= 25:
    print("Warm")
elif cel > 25:
    print("Hot")
else:
    print("Invalid input")


# 84. Simple interest vs compound interest
p=float(input("Enter principal amount: "))
r=float(input("Enter rate of interest: "))
t=float(input("Enter time: "))

a=p*(1+r/100)**t
print(a)




# 85. Number properties
num=int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0 :
    print("Negative")
elif num == 0:
    print("Zero")
else:
    print("Invalid input")

# show me prime number
