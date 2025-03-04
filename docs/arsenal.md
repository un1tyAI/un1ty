# The Arsenal: Shapesh1ft, gh0st, and N3O

This script demonstrates the power of un1ty's core AI models—**Shapesh1ft**, **gh0st**, and **N3O**—to handle creative, analytical, and technical tasks seamlessly.

## Features

1. **Shapesh1ft**: Generate creative content like text, images, or audio.
2. **gh0st**: Summarize, analyze, or translate content with precision.
3. **N3O**: Generate code, diagrams, or technical documentation for automation.

---

## Example Code

```python
import un1ty

# The Arsenal: Shapesh1ft, gh0st, and N3O

# Shapesh1ft: AI-powered creative generation
def generate_with_shapesh1ft(prompt):
    """Generate creative text, images, or audio using Shapesh1ft."""
    response = un1ty.shapesh1ft.generate(
        prompt=prompt,
        max_tokens=500
    )
    return response.text

# gh0st: AI-powered analytical processing
def summarize_with_gh0st(text):
    """Summarize, analyze, or translate content using gh0st."""
    response = un1ty.gh0st.summarize(
        text=text,
        max_tokens=100
    )
    return response.summary

# N3O: AI-powered technical automation
def generate_code_with_n3o(prompt, language="python"):
    """Generate code, diagrams, or technical documentation using N3O."""
    response = un1ty.n3o.generate_code(
        prompt=prompt,
        language=language
    )
    return response.code

# Example usage
creative_text = generate_with_shapesh1ft("Write a story about a futuristic city.")
summary = summarize_with_gh0st(creative_text)
code_snippet = generate_code_with_n3o("Write a Python function to calculate Fibonacci sequence.")

print("Creative Text:\n", creative_text)
print("Summary:\n", summary)
print("Generated Code:\n", code_snippet)
