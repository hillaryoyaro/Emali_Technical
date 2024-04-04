def k_largest(arr,k):
    n = len(arr)
    arr.sort()
    return arr[n-k]

number = [23,21,30,21,29,28,32,56,45,35]
k = 4
result =k_largest(number,k)
print(result)