file = open("F:\CODES\Python_VS\CSE221 Labs\Lab 03\input.txt", "r")
lines = file.readlines()

graph = {}

lines = [line.strip() for line in lines]
lines = [line.replace("\t", " ") for line in lines] 

for i in range(1, int(lines[0])+1):
    graph[str(i)] = []

for i in lines[2:]:
    i = i.split(" ")
        
    graph[i[0]].append(i[1])

output = open("F:\CODES\Python_VS\CSE221 Labs\Lab 03\output1.txt", "w")
output.write(str(graph))

output.close()