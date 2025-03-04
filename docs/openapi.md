# OpenAPI

un1ty’s OpenAPI is your gateway to integrating the power of the Hybr1d framework into your own applications. Designed for developers, it provides seamless access to un1ty’s AI models—Shapesh1ft, gh0st, and N3O—enabling you to build custom workflows, automate tasks, and enhance your projects with cutting-edge AI capabilities.

## Key Features
1. **Easy Integration**: Simple, RESTful API endpoints for quick setup.
2. **Multi-Model Support**: Access Shapesh1ft, gh0st, and N3O through a single API.
3. **Scalable and Secure**: Built for high-performance use cases, from small projects to enterprise-level applications.
4. **Multi-Modal Capabilities**: Generate text, images, audio, and video outputs using a unified API.

## Example Use Case
```python
import un1ty

# Initialize the un1ty API client
client = un1ty.Client(api_key="your_api_key_here")

# Generate creative text with Shapesh1ft
creative_text = client.shapesh1ft.generate(
    prompt="Write a short story about a robot exploring Mars.",
    max_tokens=300
)

# Refine the text with gh0st for clarity
refined_text = client.gh0st.summarize(
    text=creative_text,
    max_tokens=100
)

# Generate an image with Shapesh1ft
image_url = client.shapesh1ft.generate_image(
    prompt="A robot exploring the rocky terrain of Mars at sunset.",
    resolution="1024x768"
)

# Print the final outputs
print("Creative Text:", creative_text)
print("Refined Summary:", refined_text)
print("Generated Image URL:", image_url)