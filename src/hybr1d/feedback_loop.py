import un1ty

class FeedbackLoop:
    """Feedback Loop: Enhancing AI performance through user feedback."""
    
    def __init__(self, api_key):
        self.client = un1ty.Client(api_key=api_key)
    
    def collect_feedback(self, output, rating):
        """Stores user feedback to improve AI-generated results."""
        response = self.client.feedback.learn(
            output=output,
            rating=rating
        )
        return response
    
    def analyze_feedback(self):
        """Retrieves and analyzes past feedback for optimization insights."""
        response = self.client.feedback.analyze()
        return response.insights

# Example usage
if __name__ == "__main__":
    feedback_system = FeedbackLoop(api_key="your_api_key_here")
    feedback_response = feedback_system.collect_feedback("This AI-generated content was insightful!", 4.5)
    feedback_analysis = feedback_system.analyze_feedback()
    
    print("Feedback Response:\n", feedback_response)
    print("Feedback Insights:\n", feedback_analysis)