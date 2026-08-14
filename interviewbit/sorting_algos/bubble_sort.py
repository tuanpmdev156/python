def swap(arr,index1,index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

def bubble_sort(arr, n):
    for k in range(n):
        swapped = False
        for i in range(n-k-1):
            if  arr[i] > arr[i+1]:
                swap(arr, i, i+1)
                swapped = True
        if swapped:
            continue



# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
bubble_sort(arr,n) 
print ("Sorted array is:",arr)