# while condition:
# code goes here


# Simple counter
i = 1
while i <= 5:
    print(i)
    i = i + 1
# if forgot to modify i it will cause infinite loop

# while loop with user input
password = "python123"
user_input = input("Enter password: ")
while user_input != password:
    print("Wrong password, try again")
    user_input = input("Enter password: ")
print("Access granted")


# print numbers 10 to 1

num = 10
while num >= 1:
    print(num)
    num = num - 1


# say yes
text = "yes"
usr_inp = input("Say yes!!!: ")
while text != usr_inp:
    print("Not correct!!!")
    usr_inp = input("Say yes!!!: ")
print("Okay!!!")
