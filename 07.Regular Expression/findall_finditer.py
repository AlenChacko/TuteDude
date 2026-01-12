"""
====================================================
FINDING ALL MATCHES IN REGEX (findall & finditer)
====================================================

This file explains:
- What "finding all matches" means
- How re.findall() works
- How re.finditer() works
- Differences between them
- When to use which

Audience: Beginners
"""

import re


print("\n===================================")
print("1. BASIC findall()")
print("===================================")

text = "My numbers are 12, 45 and 78"
pattern = r"\d+"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("findall() result:", result)

# Explanation:
# findall() returns ALL matches as a list
# \d+ → one or more digits
# Output is a list of strings


print("\n===================================")
print("2. findall() WITH CHARACTER SET")
print("===================================")

text = "bat cat rat mat"
pattern = r"[bcr]at"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("findall() result:", result)

# Explanation:
# findall() finds every match in the string


print("\n===================================")
print("3. findall() WITH GROUPS")
print("===================================")

text = "abc123 xyz456 pqr789"
pattern = r"([a-z]+)(\d+)"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("findall() result:", result)

# Explanation:
# If the pattern has GROUPS (),
# findall() returns a list of TUPLES
# Each tuple contains the captured groups


print("\n===================================")
print("4. findall() WITHOUT GROUPS")
print("===================================")

pattern = r"[a-z]+\d+"
result = re.findall(pattern, text)
print("Pattern:", pattern)
print("findall() result:", result)

# Explanation:
# Without (), full match is returned as string


print("\n===================================")
print("5. BASIC finditer()")
print("===================================")

text = "Email1 test2 sample3"
pattern = r"\d"

result = re.finditer(pattern, text)

print("Text:", text)
print("Pattern:", pattern)
print("finditer() results:")

for match in result:
    print("Match:", match.group(), "| Start:", match.start(), "| End:", match.end())

# Explanation:
# finditer() returns an ITERATOR of match objects
# Each match object contains position info


print("\n===================================")
print("6. finditer() WITH GROUPS")
print("===================================")

text = "abc123 xyz456"
pattern = r"([a-z]+)(\d+)"

result = re.finditer(pattern, text)

for match in result:
    print("Full match:", match.group(0))
    print("Group 1:", match.group(1))
    print("Group 2:", match.group(2))
    print("Span:", match.span())
    print("-----")

# Explanation:
# group(0) → full match
# group(1), group(2) → captured groups


print("\n===================================")
print("7. findall() vs finditer() DIFFERENCE")
print("===================================")

text = "Item1 Item2 Item3"
pattern = r"Item\d"

findall_result = re.findall(pattern, text)
finditer_result = re.finditer(pattern, text)

print("findall():", findall_result)
print("finditer():")

for m in finditer_result:
    print(m.group(), "at position", m.span())

# Explanation:
# findall() → list of strings (simple)
# finditer() → match objects (powerful)


print("\n===================================")
print("8. USING finditer() FOR VALIDATION")
print("===================================")

text = "Errors: E101, E202, E303"
pattern = r"E\d{3}"

for match in re.finditer(pattern, text):
    print("Error code:", match.group(), "Position:", match.start())

# Explanation:
# Useful when positions of matches matter


print("\n===================================")
print("9. REAL-WORLD EXAMPLE: EMAIL EXTRACTION")
print("===================================")

text = "Contact us at support@test.com or admin@site.org"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)
print("Emails found using findall():", emails)

# Using finditer
print("Emails found using finditer():")
for match in re.finditer(pattern, text):
    print(match.group(), "at", match.span())


print("\n===================================")
print("SUMMARY")
print("===================================")

print(
    """
re.findall()
- Returns list
- Strings or tuples
- No position info

re.finditer()
- Returns iterator
- Match objects
- Has start(), end(), span()
"""
)

print("\n==============================")
print("END OF findall & finditer DEMO")
print("==============================")
