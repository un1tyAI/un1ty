import un1ty

# Load pre-trained model for input classification
tokenizer = un1ty.load_tokenizer("bert-base-uncased")
model = un1ty.load_model("bert-base-uncased")

# Analyze input prompt
input_prompt = "Write a Python script to analyze data and summarize the results."
inputs = tokenizer(input_prompt, return_tensors="pt")

# Classify input for task routing
outputs = model(**inputs)
task_type = "code_generation" if outputs.logits[0][0] > 0.5 else "text_generation"
print(f"Task Type: {task_type}")