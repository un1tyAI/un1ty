# Creative Studio: AI-Powered Workspace for Seamless Content Creation

The **Creative Studio** leverages un1ty's AI models—Shapesh1ft and gh0st—for generating, refining, and enhancing content such as blog posts and images.

## Example Code

```python
import un1ty

# Creative Studio: AI-powered workspace for seamless content creation

def generate_blog_post(prompt):
    """Generate a blog post using Shapesh1ft."""
    response = un1ty.shapesh1ft.generate(prompt=prompt, max_tokens=500)
    return response.text

def refine_text(text):
    """Refine text using gh0st summarization."""
    response = un1ty.gh0st.summarize(text=text, max_tokens=300)
    return response

def generate_image(prompt, resolution="1024x768"):
    """Generate an image using Shapesh1ft."""
    response = un1ty.shapesh1ft.generate_image(prompt=prompt, resolution=resolution)
    return response

# Example usage
blog_post = generate_blog_post("Write a blog post about the future of AI in healthcare.")
refined_post = refine_text(blog_post)
image_url = generate_image("A futuristic hospital with AI-powered robots assisting doctors.")

print("Blog Post:\n", refined_post)
print("Generated Image URL:\n", image_url)
