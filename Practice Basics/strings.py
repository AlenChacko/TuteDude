# 58. Concatenate two strings
first_name="Alen"
last_name="Chacko"
full_name=first_name+" "+last_name
print(full_name)

# 59. String length and indexing
language="Malayalam"
print(len(language))
print(language[0])
print(language[len(language)-1]) # or 
print(language[-1])
if language=="":
    print("EMPTY")
else:
    print(language)

# 60. Upper/lower/title
company="Infosys"
print(company.upper())
print(company.lower())
print(company.title())

# 61. Count vowels
text="Morning"
vowels="AEIOUaeiou"
count=0
for ch in text:
    for h in vowels:
        if ch in text == h in vowels:
            count=count+1
print(count)

# 62. Reverse string
name="Alen"
print(name[::-1])

# 63. Substring check
role="student"
# show mw the answer

# 64. Replace characters
message="Good morning Alen"
print(message.replace(" ","_"))

# 65. Extract digits from string
# show me the answer

# 66. Format numeric into string
name="Arjun"
score=55.676
rounded = round(score,2)
print(f"{name} scored {str(rounded)} in exam")

# 67. Escape sequences practice
# show mw the answer

# 68. Count words
# show mw the answer

# 69. First non-space char
# show mw the answer

# 70. Palindrome check
# show mw the answer