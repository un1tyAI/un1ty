import un1ty
from .input_orchestrator import classify_input
from .model_integration import integrate_models
from .collaboration_engine import combine_outputs
from .output_synthesizer import refine_output
from .feedback_loop import collect_feedback

class hybr1d:
    """Hybr1d Framework: Unifying AI models for seamless collaboration."""
    
    def __init__(self, api_key):
        self.client = un1ty.Client(api_key=api_key)
    
    def process_input(self, prompt):
        """Classifies input and routes tasks to the appropriate AI model."""
        task_type = classify_input(prompt)
        return integrate_models(prompt) if task_type else "Task type not recognized."
    
    def collaborate(self, creative_text, summary):
        """Combines outputs from different AI models for a refined result."""
        return combine_outputs(creative_text, summary)
    
    def synthesize_output(self, text, format="formal"):
        """Refines and formats AI-generated content."""
        return refine_output(text, format)
    
    def collect_feedback(self, output, rating):
        """Stores user feedback for continuous AI model improvement."""
        return collect_feedback(output, rating)

# Example usage
if __name__ == "__main__":
    hybr1d = hybr1d(api_key="your_api_key_here")
    processed_output = hybr1d.process_input("Write a blog post about AI advancements.")
    collaborative_output = hybr1d.collaborate("AI is transforming industries.", "AI has major impacts in tech and healthcare.")
    refined_text = hybr1d.synthesize_output("AI-generated content can be polished for clarity.")
    feedback_response = hybr1d.collect_feedback(refined_text, 5)
    
    print("Processed Output:", processed_output)
    print("Collaborative Output:", collaborative_output)
    print("Refined Text:", refined_text)
    print("Feedback Response:", feedback_response)
