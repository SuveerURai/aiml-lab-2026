# Question: Write a program to implement the A* algorithm.
"""A* shortest path search with an admissible heuristic."""
from heapq import heappop, heappush

def a_star(graph, heuristic, start, goal):
    frontier = [(heuristic[start], 0, start)]
    came_from = {start: None}
    cost = {start: 0}
    while frontier:
        _, g, node = heappop(frontier)
        if node == goal:
            path = []
            while node is not None:
                path.append(node); node = came_from[node]
            return path[::-1], g
        if g != cost[node]: continue
        for neighbor, weight in graph.get(node, []):
            new_cost = g + weight
            if new_cost < cost.get(neighbor, float("inf")):
                cost[neighbor] = new_cost
                came_from[neighbor] = node
                heappush(frontier, (new_cost + heuristic.get(neighbor, 0), new_cost, neighbor))
    return None, float("inf")

if __name__ == "__main__":
    graph = {"A":[("B",6),("F",3)],"B":[("C",3),("D",2)],"C":[("D",1),("E",5)],"D":[("C",1),("E",8)],"E":[("I",5),("J",5)],"F":[("G",1),("H",7)],"G":[("I",3)],"H":[("I",2)],"I":[("E",5),("J",3)],"J":[]}
    h = {"A":10,"B":8,"C":5,"D":7,"E":3,"F":6,"G":5,"H":3,"I":1,"J":0}
    path, distance = a_star(graph, h, "A", "J")
    print("Path:", path); print("Cost:", distance)
