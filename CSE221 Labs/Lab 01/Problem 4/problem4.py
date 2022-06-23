input_file = open("F:\\CODES\\Python_VS\\CSE221 Labs\\Lab 01\\Problem 4\\input.txt","r")

texts = input_file.readlines()

inputs = []
A = []
B = []

for i in texts:                               # storing inputs from file

    i = i.rstrip('\n')
    inputs.append(i)

inputs.remove('')

n = int(inputs[0])

for i in range(1, n+1):                       # populating A and B with corresponding values

    item = inputs[i].split(' ')
    A.append(item)

for j in range(n):
    for k in range(n):
        A[j][k] = int(A[j][k])

for i in range(n, 0, -1):

    item = inputs[-i].split(' ')
    B.append(item)

for j in range(n):
    for k in range(n):
        B[j][k] = int(B[j][k])


def Multiply_matrix(A,B):
  C = []
  
  for i in range(n):                            # populate C with 0s first

    row = []
    for x in range(n):
        
      row.append(0)
    C.append(row)

  for i in range(n):                             # pseudocode
    for j in range(n):
      for k in range(n):
        C[i][j] += A[i][k] * B[k][j]

  return C

C = Multiply_matrix(A,B)

output = ''
for i in C:
    for j in i:
        output += str(j) + ' '
    output += '\n'

f = open('F:\\CODES\\Python_VS\\CSE221 Labs\\Lab 01\\Problem 4\\output.txt', 'a')
f.writelines(output)
f.close