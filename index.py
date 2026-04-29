from preprocess import preprocess

def build_index(documents):
    inverted_index = {}
    
    for doc_id, text in documents.items():
        words = preprocess(text)
        
        for word in words:
            if word not in inverted_index:
                inverted_index[word] = []
            inverted_index[word].append(doc_id)
    
    return inverted_index