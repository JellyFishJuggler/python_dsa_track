n = int(input())
rgb = input()

count = 0
d = dict()

for i in range(1,len(rgb)):
    if rgb[i] == rgb[i-1]:
        count += 1

# for color in rgb:

#     if color in d:
#         d[color] += 1
#     else:
#         d[color] = 1

# for key in d.keys():
#     while d[key] % 2 != 0:
#         count += 1
#         d[key] -= 1

#     if d[key] % 2 == 0:
#         count -= 1
print(count)