def findMin(arr,i,n):
    min_index = i
    for j in range(min_index+1,n):
        if arr[j] < arr[min_index]:
            min_index = j
    return min_index

def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

def selection_sort(arr, n):
    # Recursive to compare min value with other elements
    for i in range(n):
        min_index = findMin(arr,i,n)
        if arr[i] != arr[min_index]:
            swap(arr,i,min_index)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
selection_sort(arr,n) 
print ("Sorted array is:",arr)