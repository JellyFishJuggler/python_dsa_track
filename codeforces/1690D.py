test = int(input())
n,k = map(int, input().split())

# print(strip)


for _ in range(test):

    bw = input()[:n]
    strip = list(bw)
    
    l = 0
    w = 0
    mw = 0

    for r in range(n):
        w += 1

        if r - l + 1 == k:
            mw = max(mw,w)
            w -= 1
            l += 1

print(mw)