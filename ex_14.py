numbers = [1, 2, 3, 4, 5, 6]

result = map(lambda x : x * x,numbers)

print(list(result))


numbers = [12, 5, 8, 21, 30, 17, 40]

result = filter(lambda x : x % 2 == 0 and x > 10 , numbers)

print(list(result))