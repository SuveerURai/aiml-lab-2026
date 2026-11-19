# Question: Write a program to implement the AO* algorithm.
"""AO* for an acyclic AND-OR graph. AND alternatives are child tuples."""
from functools import lru_cache

# Each node maps to alternatives: each alternative is an AND-set of children.
# A single child is an OR alternative; multiple children must all be solved.
GRAPH = {"A": [("B", "C"), ("D",)], "B": [("E", "F")], "C": [("G", "H")], "D": [("I",)], "E": [], "F": [], "G": [], "H": [], "I": []}
EDGE = {("A","B"):1,("A","C"):1,("A","D"):1,("B","E"):1,("B","F"):1,("C","G"):1,("C","H"):1,("D","I"):1}
HEURISTIC = {"A":1,"B":2,"C":2,"D":3,"E":0,"F":0,"G":0,"H":0,"I":0}

@lru_cache(None)
def solve(node):
    choices = GRAPH[node]
    if not choices: return HEURISTIC[node], ()
    scored = []
    for group in choices:
        value = sum(EDGE.get((node, child), 1) + solve(child)[0] for child in group)
        scored.append((value, group))
    return min(scored, key=lambda item: item[0])

def print_solution(node, indent=""):
    cost, group = solve(node)
    print(f"{indent}{node} (cost={cost})")
    for child in group: print_solution(child, indent + "  ")

if __name__ == "__main__":
    cost, _ = solve("A")
    print("Optimal solution graph:"); print_solution("A"); print("Optimal cost:", cost)
