n = int(input())

a = list(map(int, input().rstrip().split()))
temp = 0
count = 0
for i in range(0, n):
    for j in range(0, n-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            count = count+1

# print(a)
print("Array is sorted in", count, "swaps.")
print("First element:", a[0])
print("Last Element:", a[n-1])
