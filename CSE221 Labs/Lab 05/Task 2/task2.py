input_file = open('F:\\CODES\Python_VS\\CSE221 Labs\\Lab 05\\Task 2\\task2_input.txt', 'r')
input_data = input_file.read().splitlines()

for i in range(len(input_data)):
    input_data[i] = input_data[i].split(' ')
    for j in range(len(input_data[i])):
        input_data[i][j] = int(input_data[i][j])


def activity(n, arr, people):

    for i in range(n):
        for j in range(i+1):

            if arr[i][1] < arr[j][1]:
                arr[i], arr[j] = arr[j], arr[i]
    
    selected = []
    for i in range(people):
        new = []
        
        selected.append(arr[0])
        f = arr[0][1]
        
        # count = 0
        for c in range(len(arr)):

            if arr[c][0] >= f:
                
                f = arr[c][1]
                # count += 1
                selected.append(arr[c])
                
        for j in arr:
            if j not in selected:
                new.append(j)  
           
        arr = new

    count = len(selected)
    return count

output = open('F:\\CODES\Python_VS\\CSE221 Labs\\Lab 05\\Task 2\\task2_output.txt', 'w')

n = int(input_data[0][0])
people = int(input_data[0][1])
data = input_data[1:]

total = activity(n, data, people)

output.write(str(total))
output.close()