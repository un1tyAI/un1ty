import un1ty
import pytest

def test_classify_input():
    """Test if the Input Orchestrator correctly classifies input tasks."""
    prompt_code = "Write a Python script to analyze data."
    prompt_text = "Summarize the impact of AI in healthcare."
    
    classification_code = un1ty.hybr1d.classify(prompt_code)
    classification_text = un1ty.hybr1d.classify(prompt_text)
    
    assert classification_code in ["code_generation", "text_generation"]
    assert classification_text in ["code_generation", "text_generation"]

def test_task_routing():
    """Test if tasks are routed correctly to the appropriate AI model."""
    prompt = "Write a short story about space exploration."
    classified_task = un1ty.hybr1d.classify(prompt)
    
    if classified_task == "text_generation":
        output = un1ty.shapesh1ft.generate(prompt=prompt)
    else:
        output = None
    
    assert output is not None
    assert isinstance(output.text, str)
    assert len(output.text) > 10  # Ensuring meaningful generation

if __name__ == "__main__":
    pytest.main()
