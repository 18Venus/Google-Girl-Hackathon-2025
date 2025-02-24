import re

def get_function_names(code):
    # Regular expression pattern to match function names (e.g., def function_name(...):)
    pattern = r'def\s+(\w+)\s*\('
    
    # Find all matches in the code
    function_names = re.findall(pattern, code)
    
    return function_names

