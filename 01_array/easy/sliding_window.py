arr = [1,2,3,4,5]
k = 3

# maximum sum of any 3 consecutive elements

l = 0
w = 0
ms = 0 
for r in range(len(arr)):
    w += arr[r]
    if r - l + 1 == k:
        ms = max(ms,w)
        w -= arr[l]
        l += 1

print(f'max sum is {ms}')