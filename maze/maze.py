# -*- coding: utf-8 -*-

def dfs_iterative(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path

def dfs_recursive(graph, start, end, path=[]):
    path += [start]
    print start, end

    for neighbor in graph[start]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, end, path)

    return path


def matrix_to_graph(matrix):
    size = len(matrix)
    adj_list = {}
    pos = []
    
    for i in range(size):
        sub = []
        for j in range(size):
            sub.append(i*size+j)
        pos.append(sub)

    count = 0
    for i in range(size):
        for j in range(size):
            if(not (matrix[i][j] == 0)):
                a_list = []
                try:
                    if (matrix[i][j + 1] == 1):
                        a_list.append(pos[i][j+1])
                except:
                    pass
                
                try:        
                    if (matrix[i + 1][j] == 1):
                        a_list.append(pos[i+1][j])
                except:
                    pass
            
                adj_list[count] = a_list
            else:
                adj_list[count] = []
            count += 1
    return adj_list


def output_matrix(path, matrix):
    size = len(matrix)
    pos = []
    print path
    for i in range(size):
        for j in range(size):
            pos = i*size+j
            if(pos in path):
                matrix[i][j] = 'r'
    
    for i in matrix:
        print i


if __name__=='__main__':
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]
    
    graph = matrix_to_graph(maze)
    path = dfs_iterative(graph, 0)
    output_matrix(path, maze)
    