from preprocess import preprocess

def search(query, inverted_index):
    q_words = preprocess(query)
    results = set()
    
    for word in q_words:
        if word in inverted_index:
            results.update(inverted_index[word])
    
    return results, q_words