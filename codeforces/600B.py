n1, n2 = map(int, input().split())

a = list(map(int, input().split()))[:n1]
b = list(map(int, input().split()))[:n2]

a.sort()

c = []

for bi in b:
    left = 0
    right = n1 - 1
    count = 0

    while left <= right:
        mid = left + (right - left) // 2

        if a[mid] <= bi:
            count = mid + 1
            left = mid + 1
        else:
            right = mid - 1

    c.append(count)

print(*c)