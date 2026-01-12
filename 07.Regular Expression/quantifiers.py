"""
===========================================
REGEX QUANTIFIERS IN PYTHON (re MODULE)
===========================================

Quantifiers tell regex HOW MANY TIMES
a character, group, or character class
should appear.

This file covers:
*, +, ?, {n}, {n,}, {n,m}
Greedy vs Non-Greedy Quantifiers

Audience: Beginners
"""

import re


print("\n===================================")
print("1. STAR (*) → 0 OR MORE TIMES")
print("===================================")

text = "ca cat caaat c"
pattern = r"ca*"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# a* → 'a' can appear ZERO or MORE times
# Matches:
# 'c'     (zero a)
# 'ca'    (one a)
# 'caaat' (many a)


print("\n===================================")
print("2. PLUS (+) → 1 OR MORE TIMES")
print("===================================")

pattern = r"ca+"
result = re.findall(pattern, text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# a+ → 'a' must appear AT LEAST ONCE
# 'c' alone is NOT matched


print("\n===================================")
print("3. QUESTION MARK (?) → 0 OR 1 TIME")
print("===================================")

text = "color colour"
pattern = r"colou?r"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# u? → 'u' is OPTIONAL
# Matches both color and colour


print("\n===================================")
print("4. EXACT COUNT {n}")
print("===================================")

text = "111 11 1 1111"
pattern = r"\d{2}"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# \d{2} → EXACTLY 2 digits


print("\n===================================")
print("5. RANGE COUNT {n, m}")
print("===================================")

pattern = r"\d{2,3}"
result = re.findall(pattern, text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# \d{2,3} → minimum 2 digits, maximum 3 digits


print("\n===================================")
print("6. AT LEAST n TIMES {n,}")
print("===================================")

pattern = r"\d{3,}"
result = re.findall(pattern, text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# \d{3,} → 3 OR MORE digits


print("\n===================================")
print("7. QUANTIFIERS WITH CHARACTER SETS")
print("===================================")

text = "bat cat rat mat"
pattern = r"[bcr]at"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# [bcr] → b OR c OR r
# No quantifier here, matches once per word


print("\n===================================")
print("8. QUANTIFIERS WITH GROUPS ()")
print("===================================")

text = "ha haha hahaha"
pattern = r"(ha)+"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# (ha)+ → group 'ha' repeated one or more times


print("\n===================================")
print("9. GREEDY QUANTIFIERS (DEFAULT)")
print("===================================")

text = "<p>Hello</p><p>World</p>"
pattern = r"<p>.*</p>"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# .* is GREEDY
# It matches as MUCH text as possible
# Result: everything from first <p> to last </p>


print("\n===================================")
print("10. NON-GREEDY (LAZY) QUANTIFIERS")
print("===================================")

pattern = r"<p>.*?</p>"
result = re.findall(pattern, text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# .*? is NON-GREEDY
# It matches the SMALLEST possible text
# Each <p>...</p> is matched separately


print("\n===================================")
print("11. VALIDATION USING QUANTIFIERS")
print("===================================")

text = "Username_123"
pattern = r"^\w{5,12}$"

result = re.match(pattern, text)
print("Text:", text)
print("Pattern:", pattern)

if result:
    print("Valid username")
else:
    print("Invalid username")

# Explanation:
# ^        → start of string
# \w{5,12} → 5 to 12 word characters
# $        → end of string


print("\n===================================")
print("12. REAL-WORLD EXAMPLE: PHONE NUMBER")
print("===================================")

text = "9876543210"
pattern = r"\d{10}"

result = re.fullmatch(pattern, text)
print("Text:", text)
print("Pattern:", pattern)

if result:
    print("Valid phone number")
else:
    print("Invalid phone number")

# Explanation:
# \d{10} → exactly 10 digits


print("\n===================================")
print("SUMMARY OF QUANTIFIERS")
print("===================================")

print(
    r"""
*     → 0 or more
+     → 1 or more
?     → 0 or 1
{n}   → exactly n times
{n,}  → at least n times
{n,m} → between n and m times
*? +? ?? → non-greedy versions
"""
)

print("\n==============================")
print("END OF QUANTIFIERS DEMO")
print("==============================")
