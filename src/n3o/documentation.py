import un1ty

# N3O: AI-powered code documentation module

def generate_documentation(code_snippet):
    """Generate structured documentation for a given code snippet."""
    response = un1ty.n3o.document_code(code_snippet=code_snippet)
    return response.documentation

def explain_code(code_snippet):
    """Provide an explanation of the given code snippet for better understanding."""
    response = un1ty.n3o.explain_code(code_snippet=code_snippet)
    return response.explanation

def generate_usage_examples(code_snippet):
    """Generate example use cases for a given code snippet."""
    response = un1ty.n3o.generate_examples(code_snippet=code_snippet)
    return response.examples

# Example usage
code_snippet = """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
"""

documentation = generate_documentation(code_snippet)
explanation = explain_code(code_snippet)
usage_examples = generate_usage_examples(code_snippet)

print("Generated Documentation:", documentation)
print("Code Explanation:", explanation)
print("Usage Examples:", usage_examples)