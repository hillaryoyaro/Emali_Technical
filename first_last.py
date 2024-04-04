def first_and_last(arr,target):
    #Traverse through the array
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
        while i+1 < len(arr) and arr[i+1] == target:
            i += 1
    return [start,i]   

number = [22,29,35,40,32,27,25,24,26,28,23,22,45]
result = first_and_last(number,29)  
print(result)   