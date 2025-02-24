import ast
import nltk
from nltk.corpus import wordnet as wn

# Function to check if a word is meaningful
def is_meaningful(word):
    return bool(wn.synsets(word))

# Function to extract all comments from the code
def extract_comments(code):
    comments = []
    lines = code.splitlines()
    for line in lines:
        # Check if the line is a comment
        if line.strip().startswith("#"):
            comments.append(line.strip())  # Adding comment to list
    return comments

# Function to calculate the relevance score
def calculate_relevance(function_name, comments):
    # Get the set of meaningful words from the function name
    function_words = set(function_name.split('_'))
    meaningful_function_words = {word for word in function_words if is_meaningful(word)}
    
    relevance_score = 0
    for comment in comments:
        comment_words = set(comment.split())
        meaningful_comment_words = {word for word in comment_words if is_meaningful(word)}
        # Calculate the overlap between meaningful function words and comment words
        overlap = len(meaningful_function_words & meaningful_comment_words)
        relevance_score += overlap
    
    return relevance_score

# Function to calculate the comment quality score
def calculate_comment_quality(code, function_name):
    lines = code.splitlines()
    comments = extract_comments(code)
    
    # Debug: Check extracted comments
    print(f"Extracted Comments: {comments}")
    
    # Condition 1: Number of comments >= 1/5 of the number of lines
    num_comments = len(comments)
    num_lines = len(lines)
    print(f"Number of Comments: {num_comments}, Number of Lines: {num_lines}")
    
    comment_line_ratio = num_comments / num_lines >= 0.1 and  num_comments / num_lines<=0.4

    
    # Calculate relevance score between function name and comments
    relevance_score = calculate_relevance(function_name, comments)
    print(f"Relevance Score: {relevance_score}")
    
    # Final score calculation
    if relevance_score<1 and num_comments<=2:
        score = num_comments+relevance_score
    elif comment_line_ratio :
        score = min(relevance_score *4, 10)
    else:
        score = max(relevance_score-comment_line_ratio*3,0)
    
    return score

