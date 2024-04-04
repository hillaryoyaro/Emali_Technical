def k_largest_element(arr,k):
    #Initialize the arr and declare k as max element
    #Traverse through the maximum element:
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)   

number = [4,2,9,7,5,6,7,1,3]
result = k_largest_element(number,4)
print(result)