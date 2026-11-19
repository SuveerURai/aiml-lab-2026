# Question: Demonstrate ID3, build a decision tree from a dataset, and classify a new sample.
"""ID3 decision tree using information gain and the classic Play Tennis data."""
from collections import Counter
from math import log2

DATA = [
    {"Outlook":"sunny","Temperature":"hot","Humidity":"high","Wind":"weak","PlayTennis":"no"},
    {"Outlook":"sunny","Temperature":"hot","Humidity":"high","Wind":"strong","PlayTennis":"no"},
    {"Outlook":"overcast","Temperature":"hot","Humidity":"high","Wind":"weak","PlayTennis":"yes"},
    {"Outlook":"rain","Temperature":"mild","Humidity":"high","Wind":"weak","PlayTennis":"yes"},
    {"Outlook":"rain","Temperature":"cool","Humidity":"normal","Wind":"weak","PlayTennis":"yes"},
    {"Outlook":"rain","Temperature":"cool","Humidity":"normal","Wind":"strong","PlayTennis":"no"},
    {"Outlook":"overcast","Temperature":"cool","Humidity":"normal","Wind":"strong","PlayTennis":"yes"},
    {"Outlook":"sunny","Temperature":"mild","Humidity":"high","Wind":"weak","PlayTennis":"no"},
    {"Outlook":"sunny","Temperature":"cool","Humidity":"normal","Wind":"weak","PlayTennis":"yes"},
    {"Outlook":"rain","Temperature":"mild","Humidity":"normal","Wind":"weak","PlayTennis":"yes"},
    {"Outlook":"sunny","Temperature":"mild","Humidity":"normal","Wind":"strong","PlayTennis":"yes"},
    {"Outlook":"overcast","Temperature":"mild","Humidity":"high","Wind":"strong","PlayTennis":"yes"},
    {"Outlook":"overcast","Temperature":"hot","Humidity":"normal","Wind":"weak","PlayTennis":"yes"},
    {"Outlook":"rain","Temperature":"mild","Humidity":"high","Wind":"strong","PlayTennis":"no"},
]
TARGET = "PlayTennis"

def entropy(rows):
    n = len(rows)
    return -sum((c/n)*log2(c/n) for c in Counter(r[TARGET] for r in rows).values()) if n else 0

def build(rows, features):
    labels = [r[TARGET] for r in rows]
    if len(set(labels)) == 1: return labels[0]
    if not features: return Counter(labels).most_common(1)[0][0]
    gains = []
    for feature in features:
        vals = {r[feature] for r in rows}
        remainder = sum(sum(r[feature] == v for r in rows)/len(rows) * entropy([r for r in rows if r[feature] == v]) for v in vals)
        gains.append((entropy(rows)-remainder, feature))
    feature = max(gains)[1]
    return {feature: {v: build([r for r in rows if r[feature] == v], [f for f in features if f != feature]) for v in sorted({r[feature] for r in rows})}}

def predict(sample, tree):
    while isinstance(tree, dict):
        feature = next(iter(tree)); tree = tree[feature].get(sample.get(feature), "Unknown")
    return tree

if __name__ == "__main__":
    tree = build(DATA, ["Outlook","Temperature","Humidity","Wind"])
    sample = {"Outlook":"sunny","Temperature":"cool","Humidity":"normal","Wind":"weak"}
    print("Decision tree:", tree); print("Prediction:", predict(sample, tree))
