
import un1ty

class Summarization:
    """Summarization module using gh0st AI capabilities."""
    
    def __init__(self, api_key):
        self.client = un1ty.Client(api_key=api_key)
    
    def summarize_text(self, text, max_tokens=150):
        """Summarizes input text to provide concise information."""
        response = self.client.gh0st.summarize(
            text=text,
            max_tokens=max_tokens
        )
        return response.summary
    
    def summarize_document(self, document_path, max_tokens=200):
        """Summarizes a document by extracting key points."""
        with open(document_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        response = self.client.gh0st.summarize(
            text=content,
            max_tokens=max_tokens
        )
        return response.summary
    
    def summarize_webpage(self, url, max_tokens=200):
        """Fetches and summarizes content from a webpage."""
        response = self.client.gh0st.summarize_webpage(
            url=url,
            max_tokens=max_tokens
        )
        return response.summary

# Example usage
if __name__ == "__main__":
    summarizer = Summarization(api_key="your_api_key_here")
    summary_text = summarizer.summarize_text("Artificial Intelligence is revolutionizing the industry.")
    summary_doc = summarizer.summarize_document("document.txt")
    summary_web = summarizer.summarize_webpage("https://example.com/article")
    
    print("Text Summary:", summary_text)
    print("Document Summary:", summary_doc)
    print("Webpage Summary:", summary_web)