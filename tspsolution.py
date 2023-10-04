import sys
import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def nearest_neighbor(graph, start):
    unvisited = set(range(len(graph)))
    current_vertex = start
    path = [current_vertex]
    total_distance = 0
    
    unvisited.remove(current_vertex)
    
    while unvisited:
        nearest_vertex = min(unvisited, key=lambda vertex: graph[current_vertex][vertex])
        total_distance += graph[current_vertex][nearest_vertex]
        current_vertex = nearest_vertex
        path.append(current_vertex)
        unvisited.remove(current_vertex)
    
    # Return to the starting point to complete the cycle
    total_distance += graph[current_vertex][start]
    path.append(start)
    
    return path, total_distance

# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency matrix
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    start_vertex = 0
    path, total_distance = nearest_neighbor(graph, start_vertex)
    
    print("Optimal TSP Path:", path)
    print("Total Distance:", total_distance)
