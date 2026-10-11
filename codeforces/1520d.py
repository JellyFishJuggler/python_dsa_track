testcases = int(input())
for i in range(testcases):
    count = 0
    n = int(input())
    a = list(map(int, input().split()))[:n]

    i = 0
    while i <= len(a) - 1:
        for j in range(i+1, len(a)):
            if (a[j] - a[i]) == (j - i):
                count += 1
        i += 1
    print(count)