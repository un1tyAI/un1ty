# Translation
import un1ty

class Translation:
    """Translation module using gh0st AI capabilities."""
    
    def __init__(self, api_key):
        self.client = un1ty.Client(api_key=api_key)
    
    def translate_text(self, text, target_language="en"):
        """Translates input text into the specified target language."""
        response = self.client.gh0st.translate(
            text=text,
            target_language=target_language
        )
        return response.translation
    
    def translate_document(self, document_path, target_language="en"):
        """Translates a document into the specified target language."""
        with open(document_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        response = self.client.gh0st.translate(
            text=content,
            target_language=target_language
        )
        return response.translation
    
    def detect_language(self, text):
        """Detects the language of the given text."""
        response = self.client.gh0st.detect_language(
            text=text
        )
        return response.language

# Example usage
if __name__ == "__main__":
    translator = Translation(api_key="your_api_key_here")
    translated_text = translator.translate_text("Hello, how are you?", "es")
    translated_doc = translator.translate_document("document.txt", "fr")
    detected_language = translator.detect_language("Bonjour tout le monde")
    
    print("Translated Text:", translated_text)
    print("Translated Document:", translated_doc)
    print("Detected Language:", detected_language)
