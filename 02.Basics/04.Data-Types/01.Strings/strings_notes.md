# Python Strings — Notes (Basics → Advanced)

## 1. What is a string?
A string in Python is an immutable sequence of Unicode code points. It's the primary type for text. You can create string literals with single quotes ('...'), double quotes ("...") or triple-quoted strings for multi-line text.

## 2. Creation
- Single line: 'hello', "hello"
- Multi-line: triple-quoted strings like '''line1
line2''' or triple double-quoted strings.
- Raw strings: prefix with r"raw\n" to avoid escapes (useful for regex). Note: raw strings cannot end with a single trailing backslash.

## 3. Indexing and Slicing
- `s[i]` access single character; negative indices count from end.
- `s[start:stop:step]` slices (stop is exclusive).
- Slicing creates a new string.

## 4. Immutability
Strings are immutable. Operations that "change" a string return a new string.

## 5. Common operations
- Concatenation: `+`
- Repetition: `*`
- Membership: `'a' in s`
- Iteration: `for ch in s:`

## 6. Important built-in functions
- `len(s)`, `min(s)`, `max(s)`, `ord(ch)`, `chr(code)`, `repr(s)`, `ascii(s)`

## 7. Case conversion & checks
- Case: `lower()`, `upper()`, `title()`, `capitalize()`, `swapcase()`, `casefold()` (best for caseless matching).
- Checks: `isalpha()`, `isdigit()`, `isalnum()`, `isspace()`, `istitle()`, `isidentifier()`

## 8. Searching & count
- `s.find(sub)`, `s.rfind(sub)`, `s.index(sub)` (raises if not found), `s.count(sub)`

## 9. Replace & translate
- `s.replace(old, new[, count])` — straightforward replacement.
- `s.translate(table)` with `str.maketrans(...)` for bulk substitutions; very fast.

## 10. Splitting & Joining
- `s.split(sep=None, maxsplit=-1)`: when sep is None it splits on whitespace.
- `s.rsplit()`, `s.splitlines()`
- `sep.join(iterable)` — recommended when building strings from many pieces.

## 11. Strip & padding
- `s.strip()`, `s.lstrip()`, `s.rstrip()`
- `s.zfill(width)`, `s.center(width)`, `s.ljust(width)`, `s.rjust(width)`

## 12. Formatting text
- Old: `%` operator
- `str.format()`
- f-strings (`f"..."`) — preferred for readability and performance
- `string.Template` for safer user-substitution

## 13. Bytes & encodings
- `str.encode(encoding='utf-8')` -> bytes
- `bytes.decode(encoding='utf-8')` -> str
- Handle `errors` argument for tolerant decoding/encoding
- Use `unicodedata.normalize()` when handling combining characters

## 14. Performance
- Avoid `s += value` in loops; build a list and `''.join(list)` instead.
- `str.join()` is the idiomatic way to assemble strings from sequences.

## 15. Advanced topics
- `sys.intern()` to intern strings (saves memory with many duplicates)
- `str.maketrans()` and `translate()` for efficient mapping
- Regular expressions (`re` module) for powerful pattern matching/splitting
- `StringIO`/`BytesIO` for file-like operations on strings/bytes
- `memoryview` for zero-copy access to bytes

## 16. Practical examples (short)
- Palindrome check: clean non-alphanumerics, casefold, compare to reverse.
- Anagrams: compare sorted letters or frequency counts (`collections.Counter`).
- Extracting data: use `partition()`/`rpartition()` or `re` for complex patterns.

## 17. Troubleshooting common pitfalls
- Mixing bytes and str — always encode/decode explicitly.
- Comparing Unicode that has combining characters — normalize before comparing.
- Raw strings ending with backslash — can't end with a single trailing backslash.

## 18. Quick reference of methods
(Select most useful; see examples in the .py file.)
- `upper, lower, title, capitalize, casefold, swapcase`
- `strip, lstrip, rstrip`
- `split, rsplit, splitlines, join`
- `find, rfind, index, rindex, count`
- `startswith, endswith, replace`
- `format, zfill, center, ljust, rjust`
- `translate, maketrans`
- `isalpha, isdigit, isalnum, isspace, istitle, isidentifier`

---

## Further reading
- Python official docs: Text Sequence Type — `str`
- PEP 393 (Flexible string representation)
- `unicodedata` module docs
- `re` module docs
