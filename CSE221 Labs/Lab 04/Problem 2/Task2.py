import math
from queue import PriorityQueue


def Graph(n): 
    graph = {}
    for line in n:
        line = line.split(" ")
        

        if line[0] not in graph.keys():
            graph[line[0]] = [(int(line[1]),int(line[2]))]
            
        else:
            graph[line[0]].append((int(line[1]),int(line[2])))

        if line[1] not in graph.keys():
            graph[line[1]] = [(int(line[0]),int(line[2]))]

        else:          
            graph[line[1]].append((int(line[0]),int(line[2])))
 
    return graph


def Dijkstra(graph, source):

    if len(graph) == 0:
        return '1'

    dist = [0] * (len(graph) + 1)
    prev = [None] * (len(graph) + 1)
    Q = PriorityQueue()
    visited = [0] * (len(graph)+1) 

    for key in graph:
        if key != source:
            dist[int(key)] = math.inf
            prev[int(key)] = None
        
        Q.put((dist[int(key)], key))
        visited[int(key)] = 0

    while not Q.empty():

        u = Q.get()[1] 

        if visited[int(u)] == 1:
            continue
        visited[int(u)] = 1
 
        for v in graph[u]: 

            alt = dist[int(u)] + v[1]  
            if alt < dist[v[0]]: 
                dist[v[0]] = alt 
                prev[v[0]] = u
                Q.put((dist[v[0]], str(v[0])))
    # print(prev)
    line = len(graph) 
    path = []
    while line != 1: 
        path.append(line)      # add the node to the path
        line = int(prev[line]) # get the previous node
        
    path.append(line) 
    path.reverse() 
    # print(path)
    return path



input_file = open("F:\CODES\Python_VS\CSE221 Labs\Lab 04\Problem 2\input2.txt", "r")
inputs = input_file.readlines()
inputs = [x.strip() for x in inputs]
input_file.close()

output_file = open("F:\CODES\Python_VS\CSE221 Labs\Lab 04\Problem 2\output2.txt", "w")

count = 1
for i in range(int(inputs[0])):
    
    place = int(inputs[count].split()[1])  
    road = inputs[count+1:count+1+place] 

    graph = Graph(road)
    path = Dijkstra(graph, '1')
    for i in path:
        output_file.write(str(i) + " ")

    output_file.write(f"\n")
    count += place+1 
    
output_file.close()