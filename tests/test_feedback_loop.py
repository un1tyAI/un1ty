import un1ty
import pytest

def test_collect_feedback():
    """Test if the Feedback Loop correctly records and processes user feedback."""
    output_text = "This is a sample AI-generated text."
    user_rating = 4.5
    
    feedback_response = un1ty.feedback.learn(output=output_text, rating=user_rating)
    
    assert isinstance(feedback_response, str)
    assert "Feedback recorded" in feedback_response  # Ensure confirmation message is returned

def test_feedback_adaptation():
    """Test if the AI adapts based on collected feedback."""
    improved_output = un1ty.feedback.adapt("Generate a summary of AI advancements.")
    
    assert isinstance(improved_output, str)
    assert len(improved_output) > 10  # Ensuring feedback-driven adaptation

if __name__ == "__main__":
    pytest.main()
