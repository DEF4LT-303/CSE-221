def insertionSort(arr, arr2):

    for i in range(len(arr)-1):

        temp = arr[i+1]
        temp2 = arr2[i+1]
        j = i
        while j >= 0: # and arr[j] < temp [best case O(n)]

            if arr[j] < temp:           # decending order '<'
                arr[j+1] = arr[j]
                arr2[j+1] = arr2[j]

            else:
                break 

            j = j - 1
        arr[j+1] = temp
        arr2[j+1] = temp2 

    return arr

file = open("F:\CODES\Python_VS\CSE221 Labs\Lab 02\Problem 3\input3.txt", "r")

lines = file.readlines()                            # read the input file
array_ID = [int(i) for i in lines[1].split()]       # convert the line 2 and 3 to int array [simpler way than task 1 & 2]
array_marks = [int(i) for i in lines[2].split()]

marks_sort = insertionSort(array_marks, array_ID)   # sort marks and corresponds ID in the same order

output_file = open("F:\CODES\Python_VS\CSE221 Labs\Lab 02\Problem 3\output3.txt", "w")

for i in range(len(array_ID)):
    output_file.write(str(array_ID[i]) + " ")

output_file.close()