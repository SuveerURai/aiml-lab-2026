# Question: Use a Python library to implement Naive Bayes for classification problems.
"""Categorical Naive Bayes on the classic Play Tennis dataset (with Laplace smoothing)."""
from collections import Counter, defaultdict

ROWS = [
    ("sunny","hot","high","weak","no"),("sunny","hot","high","strong","no"),
    ("overcast","hot","high","weak","yes"),("rain","mild","high","weak","yes"),
    ("rain","cool","normal","weak","yes"),("rain","cool","normal","strong","no"),
    ("overcast","cool","normal","strong","yes"),("sunny","mild","high","weak","no"),
    ("sunny","cool","normal","weak","yes"),("rain","mild","normal","weak","yes"),
    ("sunny","mild","normal","strong","yes"),("overcast","mild","high","strong","yes"),
    ("overcast","hot","normal","weak","yes"),("rain","mild","high","strong","no"),
]
FEATURES = ("Outlook","Temperature","Humidity","Wind")

def train(rows):
    labels = Counter(row[-1] for row in rows)
    values = {i: set(row[i] for row in rows) for i in range(len(FEATURES))}
    counts = defaultdict(Counter)
    for row in rows:
        for i, value in enumerate(row[:-1]): counts[(row[-1], i)][value] += 1
    return labels, values, counts

def predict(sample, model):
    labels, values, counts = model
    import math
    scores = {}
    total = sum(labels.values())
    for label, count in labels.items():
        score = math.log(count / total)
        for i, value in enumerate(sample):
            # Laplace smoothing handles unseen feature/class combinations.
            numerator = counts[(label, i)][value] + 1
            denominator = count + len(values[i])
            score += math.log(numerator / denominator)
        scores[label] = score
    return max(scores, key=scores.get), scores

if __name__ == "__main__":
    model = train(ROWS)
    sample = ("sunny", "cool", "normal", "weak")
    label, scores = predict(sample, model)
    print("Features:", FEATURES); print("Sample:", sample)
    print("Log posterior scores:", scores); print("Predicted class:", label)
