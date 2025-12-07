d = {"a": 1, "b": 2}

d.keys()  # dict_keys(['a', 'b'])
d.values()  # dict_values([1, 2])
d.items()  # dict_items([('a', 1), ('b', 2)])

d.get("a", 0)  # 1
d.setdefault("c", 3)  # adds 'c': 3 if not exists

d.update({"b": 20, "d": 4})  # merge/update

d.pop("a")  # removes and returns value
d.popitem()  # removes and returns last key-value pair

copy_d = d.copy()  # shallow copy
d.clear()  # removes all
