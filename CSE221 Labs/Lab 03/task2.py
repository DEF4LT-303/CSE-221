from queue import Queue

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

def BFS(visited, graph, node, endPoint):

    visited[int(node)-1] = 1
    queue = Queue()
    queue.put(node)

    output.write('Places: ')

    while queue.empty() is not None:
        
        m = queue.get()
        output.write(m + ' ')

        if m == endPoint:
            break
            
        for i in graph[m]:
            
            if visited[int(i)-1] == 0:

                visited[int(i)-1] = 1
                queue.put(i)

file = open("F:\CODES\Python_VS\CSE221 Labs\Lab 03\input.txt", "r")
lines = file.readlines()

visited = [0] * int(lines[0])
graph = graph_maker(lines)

output = open("F:\CODES\Python_VS\CSE221 Labs\Lab 03\output2.txt", "w")
BFS(visited, graph, '1', '12')

output.close()