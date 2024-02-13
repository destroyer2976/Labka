ielts = [
    {"name": "Anuar", "band": "6.0"},
    {"name": "Gulya", "band": "7.5"}
]

# Adding a third person "Aruna" with band 8.0
new_person = {"name": "Aruna", "band": "8.0"}
ielts.append(new_person)

# Display the modified list
for person in ielts:
    print(f"Name: {person['name']}, Band: {person['band']}")
