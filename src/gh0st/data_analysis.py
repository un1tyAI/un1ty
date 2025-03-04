import un1ty

class DataAnalysis:
    """Data analysis module using gh0st AI capabilities."""
    
    def __init__(self, api_key):
        self.client = un1ty.Client(api_key=api_key)
    
    def analyze_dataset(self, dataset_path):
        """Analyzes structured data to extract insights."""
        response = self.client.gh0st.analyze(
            dataset=dataset_path
        )
        return response.insights
    
    def generate_summary(self, dataset_path, max_tokens=150):
        """Generates a summarized report of the dataset."""
        response = self.client.gh0st.summarize(
            text=dataset_path,
            max_tokens=max_tokens
        )
        return response.summary
    
    def detect_anomalies(self, dataset_path):
        """Detects anomalies or outliers in the dataset."""
        response = self.client.gh0st.detect_anomalies(
            dataset=dataset_path
        )
        return response.anomalies

# Example usage
if __name__ == "__main__":
    data_analyzer = DataAnalysis(api_key="your_api_key_here")
    insights = data_analyzer.analyze_dataset("data.csv")
    summary = data_analyzer.generate_summary("data.csv")
    anomalies = data_analyzer.detect_anomalies("data.csv")
    
    print("Data Insights:", insights)
    print("Summary Report:", summary)
    print("Detected Anomalies:", anomalies)