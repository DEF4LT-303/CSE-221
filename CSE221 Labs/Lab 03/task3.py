def graph_maker(lines):

    graph = {}
    lines = [line.strip() for line in lines]
    lines = [line.replace("\t", " ") for line in lines]

    for i in range(1, int(lines[0])+1):
        graph[str(i)] = []

    for i in lines[2:]:
        i = i.split(" ")
            
        graph[i[0]].append(i[1])

    return graph

printed = []
def DFS_VISIT(graph, node):

    visited[int(node)-1] = 1  
    printed.append(node) 

    for i in graph[node]: 
        if visited[int(i)-1] == 0:
            DFS_VISIT(graph, i)


def DFS(graph, endPoint):

    output.write('Places: ')

    for i in graph:
        if visited[int(i)-1] == 0: 
            DFS_VISIT(graph, i) 

    for i in printed:
        output.write(i + ' ')

        if i == endPoint:
            break


file = open("F:\CODES\Python_VS\CSE221 Labs\Lab 03\input.txt", "r")
lines = file.readlines()

visited = [0] * int(lines[0])
graph = graph_maker(lines)

output = open("F:\CODES\Python_VS\CSE221 Labs\Lab 03\output3.txt", "w")
DFS(graph, '12')

output.close()


