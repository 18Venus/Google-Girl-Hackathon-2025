import ast
import radon.complexity as rcomp

# Function to count the number of functions
def count_functions(code):
    function_count = 0
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_count += 1
    return function_count

# Function to calculate the modularity score based on code structure
def calculate_modularity_score(code):
    function_count = count_functions(code)
    code_length = len(code.splitlines())
    if code_length < 8:
        return 10
    elif code_length < 14:
        return min(max(function_count*9, 8), 10)
    elif code_length < 24:
        return min(max(function_count*3, 7), 10)
    elif code_length < 50:
        return min(function_count * 1.5, 10)
    else:
        function_score = (function_count / (code_length / 10)) * 5
        return min(function_score, 10)

