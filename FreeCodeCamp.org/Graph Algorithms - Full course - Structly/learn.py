graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def depthFirstPrint(graph, source): # abdfce
    stack = [ source ]
    
    while(len(stack)>0):
        current = stack.pop()
        print(current)
        
        for neighbour in graph[current]:
            stack.append(neighbour)

depthFirstPrint(graph, 'a')