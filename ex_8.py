text = "python is easy and python is powerful"

dic = {}

spl = text.split()

for i in spl:
    if i in dic:
        dic[i] += 1

    else:
        dic[i] = 1
print(dic)



