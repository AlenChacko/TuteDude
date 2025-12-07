person = {
    "name": "Alen",
    "age": 26,
    "place": "Cherupuzha",
    "phone": 9497226368,
    "isActive": True,
}

# adding new key-value
print(person)


# update existing key
person["isActive"] = False
print(person)

# bulk update with .update()
person.update({"country": "India", "age": 27})
print(person)


# setdefault() -> return value if key exists, if not inserts the key with a default value
gen = person.setdefault("gender", "male")
print(gen)
print(person)
# if key exists
status = person.setdefault("isActive", "Unknown")
print(status)
print(person)

# deleting entities
del person["country"]
print(person)
# if key not exists, it will raise keyError
# del person["city"]

# pop()
status = person.pop("status", "Not found")
print(status)

# popitem() -> removes last inserted item
key, value = person.popitem()
print(key, value)
print(person)


# clear()
person.clear()
print(person)
