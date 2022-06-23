import math
from os import path
from queue import PriorityQueue

# def Graph(n): 
#     graph = {}
#     for line in n:
#         line = line.split(" ")
        

#         if line[0] not in graph.keys():
#             graph[line[0]] = [(int(line[1]),int(line[2]))]
            
#         else:
#             graph[line[0]].append((int(line[1]),int(line[2])))

#         # if line[1] not in graph.keys():
#         #     graph[line[1]] = [(int(line[0]),int(line[2]))]

#         # else:          
#         #     graph[line[1]].append((int(line[0]),int(line[2])))
#     print(graph)
#     return graph


# def Dijkstra(graph, source):

#     qu = []
#     if len(graph) == 0:
#         return 0

#     dist = [0] * (len(graph) + 1)
#     prev = [None] * (len(graph) + 1)
#     Q = PriorityQueue()
#     visited = [0] * (len(graph)+1) 

#     for key in graph:
#         if key != source:
#             dist[int(key)] = math.inf
#             prev[int(key)] = None       # can skip, followed pseudo code
        
#         Q.put((dist[int(key)], key))
        
#         visited[int(key)] = 0
    
#     while not Q.empty():
    

#         u = int(Q.get()[1])     # i tried but cant get max heap out of queue library
        
#         if visited[int(u)] == 1:
#             continue
#         visited[int(u)] = 1
   
#         for v in graph[u]: 
            
#             alt = min(dist[int(u)], v[1])
#             if alt > dist[v[0]]: 
#                 dist[v[0]] = alt 
#                 prev[v[0]] = u
#                 Q.put((dist[v[0]], str(v[0])))
                
#     # print(graph)
#     return dist[len(graph)] 

import heapq
import math

def makeGraph(lines):
    graph = {}
    for line in lines:
        line = line.split(" ")
        try:
            graph[int(line[0])].append((int(line[1]),int(line[2])))
        except:
            graph[int(line[0])] = [(int(line[1]),int(line[2]))]
        
       
        if int(line[1]) not in graph:
           graph[int(line[1])] = [] 

            
    return graph



def Network(graph,source):
    dist = [-math.inf]*(len(graph)+1)
    dist[source] = 0
    q =[]
    visited = [False]*(len(graph)+1)
    prev = [None]*(len(graph)+1)
    prev[source] = 0
    
    for v in graph:
        heapq.heappush(q,(dist[v],v))
        
    heapq._heapify_max(q)

    
    while len(q)!=0:
        w,u = heapq._heappop_max(q)

        if visited[u]:
            continue
        visited[u] = True
        
        for neighbour in graph[u]:
            if w == 0 and neighbour[1] !=0:
                alt = neighbour[1]
            else:
                alt = min(w,neighbour[1])

            if alt>dist[neighbour[0]]:
                dist[neighbour[0]] = alt
                prev[neighbour[0]] = u
                heapq.heappush(q,(dist[neighbour[0]],neighbour[0]))
                heapq._heapify_max(q)
                
    for item in dist[1:]:
        if item == -math.inf:
            item = -1
        output.write(f"{item} ")
    output.write("\n")
        
    
fo = open("F:\CODES\Python_VS\CSE221 Labs\Lab 04\Problem 3\input3.txt","r")
lines = fo.read().splitlines()
fo.close()

output = open("F:\CODES\Python_VS\CSE221 Labs\Lab 04\Problem 3\output3.txt","w")
j = 1
for i in range(int(lines[0])):
    m = int(lines[j].split()[1])
    if m == 0:
        graph = {int(lines[j].split()[0]):[]}
    else:
        temp = lines[j+1:j+1+m]
        graph = makeGraph(temp)
    Network(graph,int(lines[j+1+m]))
    

    
    j += 2+m
    
output.close()


# input_file = open("F:\CODES\Python_VS\CSE221 Labs\Lab 04\Problem 3\input3.txt", "r")
# inputs = input_file.readlines()
# inputs = [x.strip() for x in inputs]
# input_file.close()

# output_file = open("F:\CODES\Python_VS\CSE221 Labs\Lab 04\Problem 3\output3.txt", "w")


# count = 1
# for i in range(int(inputs[0])):

#     connection = int(inputs[count].split()[1])
#     devices = inputs[count+1:count+1+connection]
#     source = inputs[count+1+connection]

#     graph = makeGraph(devices)
#     path = Network(graph, source)

#     output_file.write(f"{path} \n")
#     count += connection+2
    
# output_file.close()