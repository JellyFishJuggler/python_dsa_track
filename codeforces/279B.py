books,minutes = map(int, input().split())

arr = list(map(int, input().split()))[:books]

count = 0
maxCount = float('-inf')

diff = 0
for i in arr:

    diff = minutes - i

    if diff in arr:
        count += 1
    else:
        count = 1
    maxCount = max(maxCount, count)

print(maxCount)