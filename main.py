from index import build_index
from search import search
from rank import rank
from evaluate import evaluate

# -----------------------------
# DOCUMENTS (Departments)
# -----------------------------
documents = {

    "Doc1": "Public administration development management leadership governance policy",
    "Doc2": "Public relations communication media journalism strategic communication",
    "Doc3": "Sociology social anthropology society culture human behavior",
    "Doc4": "Special needs inclusive education teaching support disability education",
    "Doc5": "Business administration information systems management business technology",
    "Doc6": "Geography environmental studies earth environment climate mapping",
    "Doc7": "History heritage studies past culture archaeology history",
    "Doc8": "Logistics supply chain management transportation distribution business",
    "Doc9": "Marketing advertising branding sales business market",
    "Doc10": "Accounting finance banking money financial management",
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
