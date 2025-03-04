# gh0st Module
import un1ty

class gh0st:
    """gh0st: The Analytical Expert for summarization, data analysis, and translation."""
    
    def __init__(self, api_key):
        self.client = un1ty.Client(api_key=api_key)
    
    def summarize(self, text, max_tokens=100):
        """Summarizes input text for concise and clear output."""
        response = self.client.gh0st.summarize(
            text=text,
            max_tokens=max_tokens
        )
        return response.summary
    
    def analyze_data(self, dataset):
        """Processes and extracts insights from structured data."""
        response = self.client.gh0st.analyze(
            dataset=dataset
        )
        return response.insights
    
    def translate(self, text, target_language="en"):
        """Translates text into the specified target language."""
        response = self.client.gh0st.translate(
            text=text,
            target_language=target_language
        )
        return response.translation

# Example usage
if __name__ == "__main__":
    gh0st_client = gh0st(api_key="your_api_key_here")
    summary = gh0st_client.summarize("A long article about AI advancements...", max_tokens=100)
    insights = gh0st_client.analyze_data("dataset.csv")
    translated_text = gh0st_client.translate("Hello, world!", "es")

    print("Summarized Text:", summary)
    print("Data Insights:", insights)
    print("Translated Text:", translated_text)