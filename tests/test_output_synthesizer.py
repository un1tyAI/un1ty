import un1ty
import pytest

def test_translate_text():
    """Test if the Output Synthesizer correctly translates text."""
    text = "This is a test sentence."
    translated_text = un1ty.translate(text=text, target_language="es")
    
    assert isinstance(translated_text, str)
    assert len(translated_text) > 0  # Ensure translation is not empty

def test_format_output():
    """Test if the Output Synthesizer correctly formats content for readability."""
    text = "This is an unformatted paragraph that needs better structure."
    formatted_text = un1ty.output_synthesizer.format_text(text=text)
    
    assert isinstance(formatted_text, str)
    assert len(formatted_text) > len(text)  # Ensure enhancements are made

def test_add_metadata():
    """Test if the Output Synthesizer correctly adds metadata to generated content."""
    text = "AI-generated article about future technology."
    metadata = {"author": "AI System", "category": "Technology"}
    processed_text = un1ty.output_synthesizer.add_metadata(text=text, metadata=metadata)
    
    assert isinstance(processed_text, str)
    assert "author" in processed_text  # Ensure metadata is added

if __name__ == "__main__":
    pytest.main()