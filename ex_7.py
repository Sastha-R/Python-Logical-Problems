students = (
    ("A", 80),
    ("B", 65),
    ("C", 90),
    ("D", 72)
)
high = students[0][1]

for i in students:
    if i[1] > high:
        high = i[1]
        name = i[0]

print(name)

    