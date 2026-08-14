def merge(sub_array, left_bound, mid, right_bound):
    i = left_bound
    j = mid + 1
    temp = []

    # Compare to add smaller number
    while i <= mid and j <= right_bound:
        if sub_array[i] <= sub_array[j]:
            temp.append(sub_array[i])
            i+=1
        else:
            temp.append(sub_array[j])
            j+=1
    # Add rest numbers in left sub-array
    while i <= mid:
        temp.append(sub_array[i])
        i+=1
    # Add rest numbers in right sub-array
    while j <= right_bound:
        temp.append(sub_array[j])
        j+=1
    # Copy numbers in temp array to original array
    for k in range(left_bound, right_bound+1):
       sub_array[k] = temp[k-left_bound]

    print(sub_array)

def merge_sort(array, start, end):
    if(start >= end):
        return
    mid = (start + end)//2
    merge_sort(array, start, mid)
    merge_sort(array, mid+1, end)
    merge(array, start, mid, end)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
merge_sort(arr,0,n-1) 
print ("Sorted array is:",arr)