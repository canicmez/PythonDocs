
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]


for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")