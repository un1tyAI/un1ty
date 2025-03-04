import un1ty

class InputOrchestrator:
    """Input Orchestrator: Routes user input to the appropriate AI model."""
    
    def __init__(self, api_key):
        self.client = un1ty.Client(api_key=api_key)
        self.tokenizer = self.client.load_tokenizer("bert-base-uncased")
        self.model = self.client.load_model("bert-base-uncased")
    
    def classify_input(self, prompt):
        """Classifies user input to determine the appropriate task type."""
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model(**inputs)
        return "code_generation" if outputs.logits[0][0] > 0.5 else "text_generation"

# Example usage
if __name__ == "__main__":
    orchestrator = InputOrchestrator(api_key="your_api_key_here")
    task_type = orchestrator.classify_input("Write a Python script to analyze data and summarize the results.")
    
    print("Classified Task Type:", task_type)