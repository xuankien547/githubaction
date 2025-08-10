from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Load Hugging Face model
generator = pipeline("text-generation", model="gpt2")  # Thay model khác nếu muốn

@app.get("/")
def home():
    return {"message": "LLM API running on EKS!"}

@app.get("/generate")
def generate(prompt: str):
    result = generator(prompt, max_length=50, num_return_sequences=1)
    return {"prompt": prompt, "result": result[0]['generated_text']}
