import un1ty

# Shapesh1ft: AI-powered text generation module

def generate_text(prompt, max_tokens=500, tone="creative"):
    """Generate creative text content based on a given prompt and tone."""
    response = un1ty.shapesh1ft.generate(prompt=prompt, max_tokens=max_tokens, tone=tone)
    return response.text

def refine_text(text, style="formal"):
    """Refine AI-generated text to match a specific style (e.g., formal, casual)."""
    response = un1ty.shapesh1ft.refine_text(text=text, style=style)
    return response.refined_text

def expand_text(text, additional_context=""):
    """Expand a short piece of text with additional context for more depth."""
    response = un1ty.shapesh1ft.expand_text(text=text, additional_context=additional_context)
    return response.expanded_text

# Example usage
creative_text = generate_text("Write a short sci-fi story about space explorers.")
refined_text = refine_text(creative_text, style="poetic")
expanded_text = expand_text(creative_text, additional_context="Describe the alien planet they discover.")

print("Generated Text:", creative_text)
print("Refined Text:", refined_text)
print("Expanded Text:", expanded_text)