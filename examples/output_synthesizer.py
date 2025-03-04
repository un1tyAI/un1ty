import un1ty

# Translate output to Spanish
def translate_to_spanish(text):
    translation = un1ty.translate(
        text=text,
        target_language="es"
    )
    return translation

# Example usage
translated_output = translate_to_spanish("This is a sample output from Hybr1d.")
print(translated_output)