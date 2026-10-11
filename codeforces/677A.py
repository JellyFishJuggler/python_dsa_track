# n : no of friends
# h : height of fence

n,h = map(int, input().split())

hf = list(map(int, input().split()))[:n]

# print(f'No of friends {n} | height of fence {h} | heights of friends {hf}')

# normal persoon - 1 bent person - 2

w = 0
minwidth = float('inf')

for i in hf:
    if i <= h:
        w += 1
    else:
        w += 2
    minwidth = min(minwidth, w)
print(w)
# print(minwidth)
