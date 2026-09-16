numbers = [10, 25, 10, 30, 25, 40, 50, 30]
result = []
for i in numbers:
    if i not in result:
        result.append(i)
print(result)