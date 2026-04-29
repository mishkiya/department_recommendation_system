from preprocess import preprocess

def rank(results, documents, q_words):
    ranking = {}
    
    for doc in results:
        score = 0
        doc_words = preprocess(documents[doc])
        
        for word in q_words:
            if word in doc_words:
                score += 1
        
        ranking[doc] = score
    
    sorted_results = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_results