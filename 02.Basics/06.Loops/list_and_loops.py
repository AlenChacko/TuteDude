countries = [
    "India",
    "Australia",
    "United States",
    "Ireland",
    "Sri Lanka",
    "Iceland",
    "Cuba",
    "Iran",
    "Poland",
]
print(countries)
count = 0
count_2 = 0
for country in countries:
    if country[0] == "I":
        count += 1
print(f"Countries start with the letter 'I' : {count}")

countries_with_i = []
for country in countries:
    if country.startswith("I"):
        countries_with_i.append(country)
        count_2 += 1

print(f"Countries start with the letter 'I' : {count_2}")
print(countries_with_i)
