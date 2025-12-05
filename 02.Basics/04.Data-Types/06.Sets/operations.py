fruits = {"Apple", "Banana"}
print(f"Before adding:\n{fruits}")
# add()
fruits.add("Orange")
print(f"After adding:\n{fruits}")
# update() take multiple items in an iterable
fruits.update(["Mango", "Orange", "Cherry"])
fruit_tuple = ("Grapes", "Lemon")
fruit_list = ["Strawberry", "Guava"]
fruits.update(fruit_list)
fruits.update(fruit_tuple)
print(f"After updating:\n{fruits}")

# remove() and discard()
fruits.remove("Banana")  # error if item not found in set
print(f"After removing:\n{fruits}")
# discard()
fruits.discard("jadhfs")  # no error if the item not found
print(f"After discard:\n{fruits}")


# pop() remove random element
item = fruits.pop()
print(item)
print(f"After pop:\n{fruits}")


# clear()
fruits.clear()
print(f"After clearing:\n{fruits}")
