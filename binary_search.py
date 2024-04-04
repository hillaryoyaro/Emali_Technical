def binary_search(arr,target):
    first = 0
    last = len(arr)-1
    while first <= last:
        mid = (first + last) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            first = mid + 1
        else:
            last = mid - 1 

def verify(index):
    if index is not None:
        print("The index is found ",index)
    else:
        print("The index is not found") 

number = [20,21,22,23,24,25,26,27,28,29,30]
result = binary_search(number,35)
print(result)                      