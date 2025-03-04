import un1ty

# N3O: AI-powered code generation module

def generate_code(prompt, language="python"):
    """Generate code snippets using N3O AI."""
    response = un1ty.n3o.generate_code(prompt=prompt, language=language)
    return response.code

def optimize_code(code_snippet):
    """Optimize and improve the efficiency of a given code snippet."""
    response = un1ty.n3o.optimize_code(code_snippet=code_snippet)
    return response.optimized_code

def debug_code(code_snippet):
    """Analyze and debug a given code snippet to identify errors."""
    response = un1ty.n3o.debug_code(code_snippet=code_snippet)
    return response.debugged_code

# Example usage
code_snippet = generate_code("Write a Python function to reverse a string.")
optimized_code = optimize_code(code_snippet)
debugged_code = debug_code(optimized_code)

print("Generated Code:", code_snippet)
print("Optimized Code:", optimized_code)
print("Debugged Code:", debugged_code)
