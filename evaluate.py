def evaluate(results, relevant_docs):
    retrieved_docs = set(results)
    
    precision = len(retrieved_docs & relevant_docs) / len(retrieved_docs) if retrieved_docs else 0
    recall = len(retrieved_docs & relevant_docs) / len(relevant_docs) if relevant_docs else 0
    
    if precision + recall == 0:
        f1 = 0
    else:
        f1 = 2 * (precision * recall) / (precision + recall)
    
    return precision, recall, f1