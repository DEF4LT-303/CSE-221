input_file = open('F:\\CODES\Python_VS\\CSE221 Labs\\Lab 05\\Task 3\\task3_input.txt', 'r')
input_data = input_file.read().splitlines()

def chores(activity, character):
    
    activity = sorted(activity)
    stack = []
    index = 0
    jack = 0
    jill = 0
    sequence = ''

    for c in character:

        if c == 'J':
            jack += activity[index]
            stack.append(activity[index])
            sequence += str(activity[index])
            index += 1
            
        elif c == 'j':
            val = stack.pop()
            jill += val 
            sequence += str(val)          

    return (jack, jill, sequence)

output = open('F:\\CODES\Python_VS\\CSE221 Labs\\Lab 05\\Task 3\\task3_output.txt', 'w')

n = int(input_data[0])
arr = input_data[1].split(' ')

for i in range(len(arr)):
    arr[i] = int(arr[i])

total = chores(arr, input_data[2])

output.write(f'{total[2]} \nJack will work for {total[0]} hours \nJill will work for {total[1]} hours')
output.close()