
def largest(*values):
    lar = values[0]
    for i in values:
        if i > lar:
            lar = i
    return lar


print("largest number :",largest(10, 50, 20, 80, 30))
