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
        return 0

    dist = [0] * (len(graph) + 1)
    prev = [None] * (len(graph) + 1)
    Q = PriorityQueue()
    visited = [0] * (len(graph)+1) 

    for key in graph:
        if key != source:
            dist[int(key)] = math.inf
            prev[int(key)] = None       # can skip, followed pseudo code
        
        Q.put((dist[int(key)], key))
        visited[int(key)] = 0
    # print(Q.queue)
    while not Q.empty():

        u = Q.get()[1] # get the node with the smallest distance
        print(u) 

        if visited[int(u)] == 1:
            continue
        visited[int(u)] = 1
 
        for v in graph[u]: 
            
            alt = dist[int(u)] + v[1]          # alt = distance from source to u + distance from u to v [v[0] = node, v[1] = distance]
            if alt < dist[v[0]]:               # if the distance is smaller than the current distance
                dist[v[0]] = alt 
                prev[v[0]] = u
                Q.put((dist[v[0]], str(v[0]))) # update the priority queue
    # print(dist[-1])
    print(graph) 
    return dist[len(graph)] # returns the shortest distance from source to destination



input_file = open("F:\CODES\Python_VS\CSE221 Labs\Lab 04\Problem 1\input1.txt", "r")
inputs = input_file.readlines()
inputs = [x.strip() for x in inputs]
input_file.close()

output_file = open("F:\CODES\Python_VS\CSE221 Labs\Lab 04\Problem 1\output1.txt", "w") 

count = 1
for i in range(int(inputs[0])):
    
    place = int(inputs[count].split()[1])  
    road = inputs[count+1:count+1+place] 

    graph = Graph(road)
    titans = Dijkstra(graph, '1')
    output_file.write(f"{titans} \n")
    count += place+1 
    
output_file.close()