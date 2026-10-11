n = int(input())

names = list()

for i in range(n):
    name = input()
    names.append(name)
# print(names)

s = set()
# print(s)

for i in names:
    j = 0
    if i in s:
        print(i + str(j+ 1))
        j += 1
    else:
        s.add(i)
        print('OK')
    # j += 1