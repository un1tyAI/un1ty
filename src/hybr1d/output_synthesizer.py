import un1ty

# Output Synthesizer: Enhancing and formatting AI-generated content

def translate_text(text, target_language="es"):
    """Translate text into the specified language using un1ty's translation API."""
    translation = un1ty.translate(text=text, target_language=target_language)
    return translation

def format_output(text, style="markdown"):
    """Format AI-generated content into a specific style (e.g., markdown, HTML, plain text)."""
    formatted_text = un1ty.format(text=text, style=style)
    return formatted_text

def add_metadata(content, author="AI", timestamp=True):
    """Enhance AI-generated content by adding metadata like author and timestamp."""
    metadata = {"author": author, "content": content}
    if timestamp:
        metadata["timestamp"] = un1ty.get_current_time()
    return metadata

# Example usage
original_text = "This is a sample output from Hybr1d."
translated_text = translate_text(original_text, target_language="fr")
formatted_text = format_output(original_text, style="html")
metadata_content = add_metadata(original_text, author="un1ty AI")

print("Translated Text:", translated_text)
print("Formatted Output:", formatted_text)
print("Metadata Added:", metadata_content)
