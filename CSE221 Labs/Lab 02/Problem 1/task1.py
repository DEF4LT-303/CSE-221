## The array will be sorted for best case scenario.

def bubbleSort(arr):
    
    for i in range(len(arr)-1):

        bool = False                    # check if the array is sorted
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                bool = True

        if bool == False:           # close the loop if the array is sorted
            break




file = open("F:\CODES\Python_VS\CSE221 Labs\Lab 02\Problem 1\input1.txt", "r")

lines = file.readlines()            # read the input file
lines[1] = lines[1].split()
array = []
for i in lines[1]:
    array.append(int(i))            # convert the string to integer

bubbleSort(array)            

output_file = open("F:\CODES\Python_VS\CSE221 Labs\Lab 02\Problem 1\output1.txt", "w")

for i in array:
    output_file.write(str(i) + " ") # convert the integer to string and write to the output file

output_file.close()