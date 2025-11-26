"""
strings_practicals.py

Comprehensive practical examples for Python strings: basics -> advanced.
Run this file (or import pieces) to experiment. Each section is guarded by
if __name__ == "__main__": blocks or wrapped in functions so you can import parts.

Author: ChatGPT (GPT-5 Thinking mini)
"""


# -----------------------------------------
# SECTION 1: BASICS — creation, printing, indexing, slicing
# -----------------------------------------
def basics():
    s = "Hello, World!"
    print("Original:", s)
    print("Type:", type(s))
    print("Length:", len(s))

    # Indexing
    print("First char:", s[0])
    print("Last char:", s[-1])

    # Slicing: s[start:stop:step]
    print("Slice [0:5]:", s[0:5])
    print("Every second char:", s[::2])
    print("Reversed:", s[::-1])


# Multiline strings
multi = """This is a
multi-line string.
Line 3."""
print("Multiline:\n", multi)


# -----------------------------------------
# SECTION 2: IMMUTABILITY and common operations
# -----------------------------------------
def immutability_and_ops():
    s = "abc"
    try:
        # strings are immutable — the following will raise TypeError
        s[0] = "z"
    except TypeError as e:
        print("Immutable example (error):", e)

    # Concatenation and repetition
    a = "Hello"
    b = "World"
    print("Concat:", a + ", " + b + "!")
    print("Repeat:", "ha" * 3)

    # Membership & iteration
    print("'H' in a:", "H" in a)
    for ch in "xyz":
        print(ch, end=" ")
    print()


# -----------------------------------------
# SECTION 3: STRING METHODS — quick reference with examples
# -----------------------------------------
def methods_demo():
    s = "  Python Is Awesome!  "
    print("Original repr:", repr(s))

    # Case conversion
    print("lower():", s.lower())
    print("upper():", s.upper())
    print("title():", s.title())
    print("capitalize():", s.capitalize())
    print("swapcase():", s.swapcase())
    print("casefold() (aggressive lowercase):", s.casefold())

    # Strip whitespace
    print("strip():", s.strip())
    print("lstrip():", s.lstrip())
    print("rstrip():", s.rstrip())

    # Starts/Ends/Find/Count
    print("startswith '  Py':", s.startswith("  Py"))
    print("endswith '!  ':", s.endswith("!  "))
    print("find 'Is':", s.find("Is"))
    print("index 'Is':", s.index("Is"))  # raises if not found
    print("count 'o':", s.count("o"))

    # Replace & translate
    print("replace 'Awesome' -> 'Great':", s.replace("Awesome", "Great"))

    trans = str.maketrans("aeiou", "12345")
    print("translate vowels->numbers:", "hello".translate(trans))

    # Splitting and joining
    csv = "a,b,c,d"
    parts = csv.split(",")
    print("split(','):", parts)
    print("join back:", "-".join(parts))

    # Partition
    print("partition 'Is':", s.partition("Is"))
    print("rpartition 'Is':", s.rpartition("Is"))

    # zfill / center / ljust / rjust
    print("zfill(6):", "42".zfill(6))
    print("center(20):", "hi".center(20))
    print("rjust(6):", "42".rjust(6))
    print("ljust(6):", "42".ljust(6))

    # Checks
    for test in ["abc", "123", "abc123", "   ", "Title Case"]:
        print(
            test,
            "isalpha?",
            test.isalpha(),
            "isdigit?",
            test.isdigit(),
            "isalnum?",
            test.isalnum(),
            "isspace?",
            test.isspace(),
            "istitle?",
            test.istitle(),
        )


# -----------------------------------------
# SECTION 4: FORMATTING — %, str.format, f-strings, Template
# -----------------------------------------
def formatting_examples():
    name = "Alice"
    score = 93.4567

    # %-formatting (old)
    print("Hello, %s. Score: %.2f" % (name, score))

    # str.format()
    print("Hello, {}. Score: {:.1f}".format(name, score))
    print("Named: {n} -> {s:.3f}".format(n=name, s=score))

    # f-strings (Python 3.6+)
    pi = 3.14159
    print(f"Pi rounded: {pi:.2f}")
    print(f"User {name!r} has score {score:.1f}")  # !r uses repr()

    # Advanced f-string expressions
    values = [1, 2, 3]
    print(f"sum={sum(values):d}, joined={'|'.join(map(str,values))}")

    # Template strings (safer for user-supplied formats)
    from string import Template

    t = Template("Hello, $who! You have $$${amount}.")
    print(t.substitute(who=name, amount="100"))


# -----------------------------------------
# SECTION 5: ENCODING / BYTES / UNICODE
# -----------------------------------------
def encoding_examples():
    s = "café — 東京"
    print("Original:", s)

    # Encode to bytes (utf-8)
    b = s.encode("utf-8")
    print("Bytes:", b)
    print("Decode back:", b.decode("utf-8"))

    # Handling errors
    try:
        print(b.decode("ascii"))
    except UnicodeDecodeError as e:
        print("Decode error (expected):", e)

    # Using errors parameter
    print("ascii with errors='ignore':", b.decode("ascii", errors="ignore"))

    # ord / chr
    print("ord('A'):", ord("A"))
    print("chr(9731):", chr(9731))  # snowman

    # normalization (unicodedata)
    import unicodedata

    s1 = "e\u0301"  # 'e' + combining acute
    s2 = "\u00e9"  # 'é' single codepoint
    print("Same visual?", s1, s2)
    print(
        "NFC equal?",
        unicodedata.normalize("NFC", s1) == unicodedata.normalize("NFC", s2),
    )


# -----------------------------------------
# SECTION 6: PERFORMANCE TIPS
# -----------------------------------------
def performance_tips():
    # Avoid repeated concatenation in loops
    import time

    n = 10000

    t0 = time.time()
    s = ""
    for i in range(n):
        s += "x"
    t1 = time.time()
    print("Concat in loop time:", t1 - t0)

    t0 = time.time()
    s = ["x"] * n
    s = "".join(s)
    t1 = time.time()
    print("Join time:", t1 - t0)


# -----------------------------------------
# SECTION 7: ADVANCED — translate, maketrans, unicode names, intern
# -----------------------------------------
def advanced_examples():
    # translate & maketrans for bulk replacements
    table = str.maketrans({"a": "@", "e": "3", "i": "1"})
    print("translate:", "apples and bananas".translate(table))

    # unicode names
    import unicodedata

    print("Unicode name for '©':", unicodedata.name("©"))

    # intern strings (useful for many identical immutable strings)
    import sys

    a = sys.intern("this is a long string used many times")
    b = sys.intern("this is a long string used many times")
    print("Same object after intern?:", a is b)


# -----------------------------------------
# SECTION 8: REGEX with strings (re)
# -----------------------------------------
def regex_with_strings():
    import re

    text = "Contact: alice@example.com, bob99@test.org; carol@site.co.uk"
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}", text)
    print("Emails found:", emails)

    # split with regex
    parts = re.split(r"[;,\s]\s*", text)
    print("Regex split:", parts)

    # search vs match
    m = re.search(r"\w+@[\w.]+", text)
    if m:
        print("First email:", m.group(0))


# -----------------------------------------
# SECTION 9: ADVANCED MANIPULATION — StringIO, bytes <-> str, memoryview
# -----------------------------------------
def advanced_manipulation():
    from io import StringIO, BytesIO

    s = "line1\nline2\nline3"
    f = StringIO(s)
    print("StringIO readlines:", f.readlines())

    b = b"hello bytes"
    bio = BytesIO(b)
    print("BytesIO read:", bio.read())

    # memoryview on bytes (not on str)
    m = memoryview(b)
    print("memoryview slice:", m[0:5].tobytes())


# -----------------------------------------
# SECTION 10: PRACTICAL EXERCISES (functions you can reuse)
# -----------------------------------------
def is_palindrome(s: str) -> bool:
    """Check palindrome (ignore case and non-alphanumeric)."""
    import re

    cleaned = re.sub(r"[^A-Za-z0-9]", "", s).casefold()
    return cleaned == cleaned[::-1]


def find_anagrams(word, candidates):
    """Return anagrams of 'word' from candidates (case-insensitive)."""
    key = sorted(word.casefold())
    return [c for c in candidates if sorted(c.casefold()) == key]


def most_frequent_char(s):
    """Return (char, count) of the most frequent non-space character."""
    from collections import Counter

    s2 = s.replace(" ", "")
    c = Counter(s2)
    if not c:
        return None, 0
    ch, cnt = c.most_common(1)[0]
    return ch, cnt


# -----------------------------------------
# SECTION 11: DEMO RUN (if run as script)
# -----------------------------------------
if __name__ == "__main__":
    print("=== BASICS ===")
    basics()
    print("\n=== IMMUTABILITY & OPS ===")
    immutability_and_ops()
    print("\n=== METHODS DEMO ===")
    methods_demo()
    print("\n=== FORMATTING ===")
    formatting_examples()
    print("\n=== ENCODING ===")
    encoding_examples()
    print("\n=== PERFORMANCE ===")
    performance_tips()
    print("\n=== ADVANCED ===")
    advanced_examples()
    print("\n=== REGEX ===")
    regex_with_strings()
    print("\n=== ADV MANIP ===")
    advanced_manipulation()
    print("\n=== PRACTICALS ===")
    print(
        "is_palindrome('A man, a plan, a canal: Panama') ->",
        is_palindrome("A man, a plan, a canal: Panama"),
    )
    print(
        "find_anagrams('eat', ['tea','tan','ate','nat','bat']) ->",
        find_anagrams("eat", ["tea", "tan", "ate", "nat", "bat"]),
    )
    print("most_frequent_char('abbccc dddde') ->", most_frequent_char("abbccc dddde"))
