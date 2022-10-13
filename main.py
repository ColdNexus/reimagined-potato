def prin(arr):
    for i in range(len(arr)):
        print(i+1, arr[i])

a = [5, 9, 11, 3, 8, 10, 2, 12, 7, 4, 6, 1]
b = a.copy()
pw = 148
for _ in range(pw-1):
    t = [0]*len(a)
    for i in range(len(a)):
        t[i] = b[a[i]-1]
    a = t
prin(a)