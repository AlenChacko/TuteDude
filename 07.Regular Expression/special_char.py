"""
=================================================
REGEX SPECIAL CHARACTERS IN PYTHON (re MODULE)
=================================================

Special characters are predefined shortcuts in regex
that represent common character groups like digits,
letters, spaces, word boundaries, etc.

Audience: Beginners
"""

import re


print("\n===================================")
print("1. \\d → DIGITS (0–9)")
print("===================================")

text = "My age is 25 and my brother is 30"
pattern = r"\d"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# \d → matches any digit from 0 to 9


print("\n===================================")
print("2. \\D → NON-DIGITS")
print("===================================")

pattern = r"\D"
result = re.findall(pattern, text)
print("Pattern:", pattern)
print("Matches (first 20):", result[:20])

# Explanation:
# \D → anything that is NOT a digit


print("\n===================================")
print("3. \\w → WORD CHARACTERS")
print("===================================")

text = "Python_3 is awesome!"
pattern = r"\w"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# \w → letters (a-z, A-Z), digits (0-9), underscore (_)


print("\n===================================")
print("4. \\W → NON-WORD CHARACTERS")
print("===================================")

pattern = r"\W"
result = re.findall(pattern, text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# \W → symbols, spaces, punctuation


print("\n===================================")
print("5. \\s → WHITESPACE")
print("===================================")

text = "Hello   World\tPython\nRegex"
pattern = r"\s"

result = re.findall(pattern, text)
print("Text:", repr(text))
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# \s → spaces, tabs, newlines


print("\n===================================")
print("6. \\S → NON-WHITESPACE")
print("===================================")

pattern = r"\S"
result = re.findall(pattern, text)
print("Pattern:", pattern)
print("Matches (first 20):", result[:20])

# Explanation:
# \S → characters that are NOT whitespace


print("\n===================================")
print("7. WORD BOUNDARY \\b")
print("===================================")

text = "cat scatter cater"
pattern = r"\bcat\b"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# \b → word boundary
# Matches 'cat' only as a complete word


print("\n===================================")
print("8. NOT WORD BOUNDARY \\B")
print("===================================")

pattern = r"\Bcat\B"
result = re.findall(pattern, text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# \B → NOT a word boundary
# Matches 'cat' inside another word


print("\n===================================")
print("9. ESCAPING SPECIAL CHARACTERS")
print("===================================")

text = "The price is $100.50"
pattern = r"\$"

result = re.search(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Match:", result.group())

# Explanation:
# $ is special in regex
# \$ means literal dollar sign


print("\n===================================")
print("10. MATCHING A DOT (.)")
print("===================================")

text = "file.txt backup.txt"
pattern = r"\.txt"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# . is special
# \. matches a literal dot


print("\n===================================")
print("11. USING ^ AND $ TO VALIDATE STRING")
print("===================================")

text = "Python123"
pattern = r"^\w+$"

result = re.match(pattern, text)
print("Text:", text)
print("Pattern:", pattern)

if result:
    print("Valid string")
else:
    print("Invalid string")

# Explanation:
# ^ → start
# $ → end
# \w+ → only word characters allowed


print("\n===================================")
print("12. REPLACING SPECIAL CHARACTERS")
print("===================================")

text = "Hello@World#Python!"
pattern = r"\W"
replacement = ""

result = re.sub(pattern, replacement, text)
print("Text:", text)
print("Result:", result)

# Explanation:
# \W → remove non-word characters


print("\n===================================")
print("SUMMARY OF SPECIAL CHARACTERS")
print("===================================")

print(
    r"""
\d  → digit
\D  → non-digit
\w  → word character
\W  → non-word character
\s  → whitespace
\S  → non-whitespace
\b  → word boundary
\B  → not word boundary
\.  → literal dot
\$  → literal dollar sign
"""
)

print("\n==============================")
print("END OF SPECIAL CHARACTERS DEMO")
print("==============================")
