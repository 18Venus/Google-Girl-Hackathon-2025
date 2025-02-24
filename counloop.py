import ast
import radon.complexity as rcomp

# Function to count the number of loops (for, while)
def count_loops(code):
    loop_count = 0
    for node in ast.walk(ast.parse(code)):
        if isinstance(node, (ast.For, ast.While)):
            loop_count += 1
    return loop_count