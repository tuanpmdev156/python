# Iterative
def binary_search_1(arr,target,left,right):
    while left <= right:
        #mid = (left + right) // 2 - Overflow possible
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1  
      

# Recursive
def binary_search_2(arr,target,left,right):
    if left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_2(arr,target,left,mid - 1)
        else:
            return binary_search_2(arr,target,mid + 1,right)
    return -1


# Driver code to test above 
arr = [1, 2, 6, 9, 10, 16]
search_num = 2
n = len(arr)
found_index = binary_search_2(arr,search_num,0,n-1) 
print (f"Index of {search_num} is:", found_index)