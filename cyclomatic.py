import ast
import radon.complexity as rcomp

# Function to calculate cyclomatic complexity
def calculate_cyclomatic_complexity(code):
    parsed = ast.parse(code)
    complexity = rcomp.cc_visit(parsed)
    return complexity[0].complexity
