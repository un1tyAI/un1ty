import un1ty

# N3O: AI-powered debugging module

def debug_code(code_snippet):
    """Analyze and debug a given code snippet to identify and fix errors."""
    response = un1ty.n3o.debug_code(code_snippet=code_snippet)
    return response.debugged_code

def explain_bug(code_snippet):
    """Provide explanations and insights into the detected bugs."""
    response = un1ty.n3o.explain_bug(code_snippet=code_snippet)
    return response.explanation

def suggest_fixes(code_snippet):
    """Suggest code fixes and improvements based on identified bugs."""
    response = un1ty.n3o.suggest_fixes(code_snippet=code_snippet)
    return response.suggested_fixes

# Example usage
code_snippet = "def add_numbers(a, b):\n return a + b\nprint(add_numbers(5))"
debugged_code = debug_code(code_snippet)
explanation = explain_bug(code_snippet)
suggested_fixes = suggest_fixes(code_snippet)

print("Debugged Code:", debugged_code)
print("Bug Explanation:", explanation)
print("Suggested Fixes:", suggested_fixes)