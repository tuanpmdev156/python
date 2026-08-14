
def swap(arr,index1,index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

# Lomuto's method
def partition(arr, low, high):
    i = low - 1
    pivot = high
    for j in range(low,high):
        if(arr[j] < arr[pivot]):
            i += 1
            swap(arr,i,j)
    swap(arr,i+1,pivot)
    return i + 1

# Hoere's method
#################################
     


def quick_sort(arr, low, high):
    # Infinite loop - why low always smaller than high ? 
    #while(low < high):
    if low < high:                
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot + 1, high)
    

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quick_sort(arr,0,n-1) 
print ("Sorted array is:",arr)