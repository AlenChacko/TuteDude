students = {
    "s1": {"name": "Alen", "age": 23, "marks": 90},
    "s2": {"name": "Riya", "age": 22, "marks": 95},
}

print(students["s1"]["name"])  # 'Alen'
print(students["s2"]["marks"])  # 95

# updating
students["s1"]["marks"] = 92
students["s2"]["city"] = "Kochi"


# looping
for sid, info in students.items():
    print("ID:", sid)
    for key, value in info.items():
        print("  ", key, "=", value)
