import un1ty
# Add a new AI model to the framework
def add_new_model(model_name, api_key):
    un1ty.integrate_model(
        name=model_name,
        api_key=api_key
    )
    return f"Model {model_name} integrated successfully."

# Example usage
add_new_model("N3O", "your-api-key-here")