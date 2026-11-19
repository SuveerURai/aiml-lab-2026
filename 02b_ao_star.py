# Question: Write a program to implement the AO* algorithm.
"""AO* search on an explicit, acyclic AND-OR graph."""

# Each alternative is an AND-set of children; alternatives are joined by OR.
GRAPH = {
    "A": [("B", "C"), ("D",)],
    "B": [("E", "F")], "C": [("G", "H")], "D": [("I",)],
    "E": [], "F": [], "G": [], "H": [], "I": [],
}
EDGE_COST = {
    ("A", "B"): 1, ("A", "C"): 1, ("A", "D"): 1,
    ("B", "E"): 1, ("B", "F"): 1,
    ("C", "G"): 1, ("C", "H"): 1, ("D", "I"): 1,
}
HEURISTIC = {"A": 1, "B": 2, "C": 2, "D": 3, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0}

def ao_star(start):
    """Expand the current best partial solution and back up costs to the root."""
    estimate = dict(HEURISTIC)
    expanded = {start}
    solved = set()
    best = {}

    def backup_all():
        changed = True
        while changed:
            changed = False
            for node in reversed(tuple(expanded)):
                choices = GRAPH[node]
                if not choices:
                    if node not in solved:
                        solved.add(node); estimate[node] = 0; changed = True
                    continue
                choice = min(choices, key=lambda group: sum(
                    EDGE_COST.get((node, child), 1) + estimate[child] for child in group
                ))
                value = sum(EDGE_COST.get((node, child), 1) + estimate[child] for child in choice)
                if best.get(node) != choice or estimate[node] != value:
                    best[node] = choice; estimate[node] = value; changed = True
                if all(child in solved for child in choice) and node not in solved:
                    solved.add(node); changed = True

    def next_unexpanded(node, visited):
        if node in visited or node in solved: return None
        visited.add(node)
        if node not in expanded: return node
        for child in best.get(node, ()):
            candidate = next_unexpanded(child, visited)
            if candidate is not None: return candidate
        return None

    while start not in solved:
        backup_all()
        leaf = next_unexpanded(start, set())
        if leaf is None: break
        print("Expanding:", leaf)
        expanded.add(leaf)
        if not GRAPH[leaf]: solved.add(leaf)
    backup_all()
    return estimate[start], best

def print_solution(node, best, indent=""):
    print(f"{indent}{node}")
    for child in best.get(node, ()): print_solution(child, best, indent + "  ")

if __name__ == "__main__":
    cost, choices = ao_star("A")
    print("Optimal solution graph:")
    print_solution("A", choices)
    print("Optimal cost:", cost)
