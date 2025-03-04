import un1ty
import pytest

def test_model_integration():
    """Test if Hybr1d correctly integrates multiple AI models for seamless workflow."""
    prompt = "Write a technical blog post about AI ethics."
    
    # Generate initial content with Shapesh1ft
    creative_text = un1ty.shapesh1ft.generate(prompt=prompt, max_tokens=500)
    
    # Summarize with gh0st
    summarized_text = un1ty.gh0st.summarize(text=creative_text, max_tokens=200)
    
    # Generate technical insights with N3O
    code_snippet = un1ty.n3o.generate_code(prompt="Write a Python function for sentiment analysis.", language="python")
    
    assert isinstance(creative_text, str)
    assert len(creative_text) > 50  # Ensure meaningful text generation
    
    assert isinstance(summarized_text, str)
    assert len(summarized_text) > 20  # Ensure summarization retains key points
    
    assert isinstance(code_snippet, str)
    assert "def" in code_snippet  # Ensure valid Python function generation

if __name__ == "__main__":
    pytest.main()