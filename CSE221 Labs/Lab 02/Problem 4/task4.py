''' NOTE: I was having trouble understanding the pseudocode,
        so i took help from google understanding the following code. '''         

def merge(arr, p, q):

    left = len(p)
    right = len(q)

    i = j = k = 0                   # i, j, k are the indexes of the left, right, merged arrays respectively

    while i < left and j < right:   # compare left most elements of left and right arrays

        if p[i] < q[j]:             # save the smaller element in the merged array
            arr[k] = p[i]
            i += 1

        else:
            arr[k] = q[j]
            j += 1
        
        k += 1                      # update index of merged array

    while i < left:                 # if there are still elements in the left array
        arr[k] = p[i]
        i += 1
        k += 1

    while j < right:                # if there are still elements in the right array
        arr[k] = q[j]
        j += 1
        k += 1

def merge_sort(arr):

    if len(arr) <= 1:               # base case
        return arr
        
    mid = len(arr) // 2             # find midpoint and split arrays
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)                # recursively sort left and right arrays
    merge_sort(right)

    merge(arr, left, right)         # merge the two sorted arrays

file = open("F:\CODES\Python_VS\CSE221 Labs\Lab 02\Problem 4\input4.txt", "r")

lines = file.readlines()

size = int(lines[0])
array = [int(i) for i in lines[1].split()]

merge_sort(array)

output = open("F:\CODES\Python_VS\CSE221 Labs\Lab 02\Problem 4\output4.txt", "w")

for i in range(size):
    output.write(str(array[i]) + " ")

output.close()