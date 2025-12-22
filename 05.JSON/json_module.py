# importing json module

import json

# json.dumps() -> Converts python object to json strings

data = {"name": "Alen", "age": 26, "place": "Cherupuzha", "phone": 9497226368}

json_data = json.dumps(data)
print(json_data)
print(type(json_data))


# json.loads() -> Converts json string to python object
person = """
{
  "name": "Alen",
  "age": 25,
  "isDeveloper": true,
  "skills": ["Python", "JavaScript"],
  "address": {
    "city": "Kochi",
    "country": "India"
  }
}
"""

person_data = json.loads(person)
print(person_data)
print(type(person_data))


# python to json file using dump()

student = {"name": "Albin", "class": "10th", "gender": "male", "is_passed": True}

with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    content = file.read()
    print(content)
