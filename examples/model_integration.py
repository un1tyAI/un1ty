import un1ty

# Route input to Shapesh1ft for creative writing
def generate_with_shapesh1ft(prompt):
    response = un1ty.shapesh1ft.generate(
        prompt=prompt,
        max_tokens=500
    )
    return response.text

# Route input to gh0st for summarization
def summarize_with_gh0st(text):
    response = un1ty.gh0st.summarize(
        text=text,
        max_tokens=100
    )
    return response.summary

# Example usage
creative_text = generate_with_shapesh1ft("Write a story about a futuristic city.")
summary = summarize_with_gh0st(creative_text)
print(summary)