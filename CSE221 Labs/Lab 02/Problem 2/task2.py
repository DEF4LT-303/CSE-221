def selectionSort(arr):

    for i in range(len(arr)):

        min_index = i                       # initialize the minimum index
        for j in range(i+1, len(arr)):

            if arr[min_index] > arr[j]:
                min_index = j               # update the minimum index if the current element is smaller
        arr[i], arr[min_index] = arr[min_index], arr[i] 

    return arr

file = open("F:\CODES\Python_VS\CSE221 Labs\Lab 02\Problem 2\input2.txt", "r")

lines = file.readlines()            # read the input file
lines[1] = lines[1].split()
output_range = int(lines[0][2])     # get the output range

array = []
for i in lines[1]:
    array.append(int(i))            # convert the string to integer

selectionSort(array)

output_file = open("F:\CODES\Python_VS\CSE221 Labs\Lab 02\Problem 2\output2.txt", "w")

for i in range(output_range):
    output_file.write(str(array[i]) + " ") # convert the integer to string and write to the output file

output_file.close()
