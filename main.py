from index import build_index
from search import search
from rank import rank
from evaluate import evaluate

# -----------------------------
# DOCUMENTS (Departments)
# -----------------------------
documents = {
    "Doc1": "Computer science department involves programming coding algorithms and data structures",
    "Doc2": "Information technology department focuses on networking databases and system administration",
    "Doc3": "Electrical engineering department deals with circuits electronics and power systems",
    "Doc4": "Mechanical engineering department includes machines thermodynamics and manufacturing",
    "Doc5": "Business administration department covers management marketing finance and entrepreneurship"
}

# -----------------------------
# BUILD INDEX
# -----------------------------
index = build_index(documents)

print("Inverted Index:")
print(index)

# -----------------------------
# QUERY
# -----------------------------
query = input("Enter your interest: ")

# -----------------------------
# SEARCH
# -----------------------------
results, q_words = search(query, index)

print("\nSearch Results:", results)

# -----------------------------
# RANKING
# -----------------------------
ranked = rank(results, documents, q_words)

print("\nRecommended Departments:")
for doc, score in ranked:
    print(doc, "->", documents[doc], "(Score:", score, ")")

# -----------------------------
# EVALUATION (Example)
# -----------------------------
relevant_docs = {"Doc1"}  # change depending on query

precision, recall, f1 = evaluate(results, relevant_docs)

print("\nEvaluation:")
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)