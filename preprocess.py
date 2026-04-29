def preprocess(text):
    text = text.lower()
    words = text.split()
    
    stopwords = ["is", "an", "the", "and", "of", "on"]
    words = [w for w in words if w not in stopwords]
    
    return words