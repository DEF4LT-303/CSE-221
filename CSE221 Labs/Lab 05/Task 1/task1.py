input_file = open('F:\\CODES\Python_VS\\CSE221 Labs\\Lab 05\\Task 1\\task1_input.txt', 'r')
input_data = input_file.read().splitlines()

for i in range(1, len(input_data)):
    input_data[i] = input_data[i].split(' ')
    for j in range(len(input_data[i])):
        input_data[i][j] = int(input_data[i][j])

arr = input_data[1:]

def Assignment_Selection(arr, n):

    for i in range(n):
        for j in range(i+1):

            if arr[i][1] < arr[j][1]:
                arr[i], arr[j] = arr[j], arr[i]

    selected = []
    selected.append(arr[0])
    
    count = 1

    f = arr[0][1]
    
    for c in range(n):
 
        if arr[c][0] >= f:

            f = arr[c][1]
            count += 1
            selected.append(arr[c])
            
    return (count, selected)

output = open('F:\\CODES\Python_VS\\CSE221 Labs\\Lab 05\\Task 1\\task1_output.txt', 'w')

n = int(input_data[0])

total = Assignment_Selection(arr, n)
# print(total)

output.write(str(total[0]))
for i in range(len(total[1])):
    output.write('\n')

    for j in range(2):
        output.write(str(total[1][i][j]) + ' ')

output.close()
