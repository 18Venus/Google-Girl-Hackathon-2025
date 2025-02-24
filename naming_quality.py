import nltk
from nltk.corpus import wordnet as wn

# Function to check if a word is meaningful
def is_meaningful(word):
    # Check if the word exists in WordNet
    return bool(wn.synsets(word))

# Function to calculate naming quality score
def calculate_naming_quality(function_name):
    words = function_name.split('_')
    meaningful_words = [word for word in words if is_meaningful(word)]
    meaningful_word_count = len(meaningful_words)
    

    score = meaningful_word_count * 3

    if(len(words)<=2):
        score=score+2
 
    elif (len(words)<=4):
        score=min(score,10)
    else:
        
        score = max(score - (len(words) - 4) * 2, 0)
    
    return score
