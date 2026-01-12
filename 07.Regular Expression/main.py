import re

text = "I love Python"

# re.search()

# return match object
result = re.search(r"Python", text)
print(result)

# if a match exists
print(result.group())
print(result.start())
print(result.end())

# return None
result = re.search(r"Node", text)
print(result)


# re.match()
text = "I am a developer"

# return None
result = re.match(r"developer", text)
print(result)

# return match object
result = re.match(r"I am", text)
print(result)


# re.findall()
text = "I have 2 cats and 3 dogs"

# [ '2', '3']
result = re.findall(r"\d", text)
print(result)


# re.finditer()
text = "I was born in 1999, I have 2 sim cards.\nAlso I have 2 smartphones and 1 laptop"
for match in re.finditer(r"\d", text):
    print(match.group(), match.start())


message = (
    "The current Python version is 3.13. Other previous versions are 3.12, 3.11, 3.10"
)

match_object = re.search("[0-9][0-9]", message)
print(match_object)
match_object = re.search("[0-9][0-9]", "House number 25134")
print(match_object)
match_object = re.search("[0-9][0-9][0-9]", "This number is 22.345 and 654.32")
print(match_object)


# dot
match_object = re.search("[0-9].[0-9][0-9]", "What about dot - 3.23")
print(match_object)
# dot match any character except a new line
match_object = re.search("[0-9].[0-9]", "House number 251/A")
print(match_object)
# to fix that
match_object = re.search("[0-9].[0-9][0-9]", "This will fix dot 2011")
print(match_object)
# to
match_object = re.search("[0-9][.][0-9][0-9]", "This will fix dot 2011")
print(match_object)
