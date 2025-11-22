# Python Type Conversion Practicals (Complete)

# 1. Implicit Conversion
a = 5
b = 2.5
result = a + b
print(result)
print(type(result))

a = True
b = a + 5
print(b)
print(type(b))

c = b + 0.5
print(c)
print(type(c))

a = 10
b = 3 + 2j
print(a + b)

a = 2.5
b = 3 + 4j
print(a + b)

# 2. Explicit Type Conversion

# TO INTEGER
print(int(5.9))
print(int(-2.3))
print(int(True))
print(int(False))
print(int("10"))
print(int("250"))

# TO FLOAT
print(float(10))
print(float("10.5"))
print(float("20"))
print(float(True))
print(float(False))

# TO STRING
print(str(10))
print(str(3.14))
print(str(True))
print(str([1,2,3]))
print(str({"a":1,"b":2}))
print(str({1,2,3}))

# TO LIST
print(list("abc"))
print(list((1,2,3)))
print(list({10,20,30}))
print(list({"name":"Alen","age":21}))
print(list(range(5)))

# TO TUPLE
print(tuple([1,2,3]))
print(tuple("ABC"))
print(tuple({10,20,30}))

# TO SET
print(set([1,2,2,3]))
print(set((10,20,20,30)))
print(set("hello"))

# TO DICT
print(dict([("a",1),("b",2)]))
print(dict((("x",10),("y",20))))

# RANGE
print(list(range(5)))
print(list(range(2,10,2)))

# BYTES
print(bytes([65,66,67]))
print("Hello".encode())

# BYTEARRAY
ba = bytearray([65,66,67])
print(ba)
ba[0] = 90
print(ba)

# FROZENSET
print(frozenset([1,2,3,3]))
print(frozenset({10,20,30}))

# Advanced Conversions
print(bool(""))
print(bool("hi"))

lst = ["a","b","c"]
print("".join(lst))

text = "a b c"
print(text.split())

d = {"a":1,"b":2}
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))
