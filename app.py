"""Compare responses from multiple local Ollama models side by side."""
import time
from concurrent.futures import ThreadPoolExecutor
import streamlit as st
import ollama

MODELS = [
    "qwen2.5-coder-7b-instruct-q5_k_m",
    "phi-4-mini-instruct-q4_k_m",
    "gemma-4-e4b-it.q5_k_m",
]

st.set_page_config(page_title="Ollama Model Arena", layout="wide")
st.title("Ollama Model Arena")

prompt = st.text_area("Prompt", height=100)
run = st.button("Run on all models")


def query_model(model: str, prompt: str):
    start = time.time()
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    elapsed = time.time() - start
    return model, response["message"]["content"], elapsed


if run and prompt.strip():
    with st.spinner("Querying all models..."):
        with ThreadPoolExecutor(max_workers=len(MODELS)) as executor:
            results = list(executor.map(lambda m: query_model(m, prompt), MODELS))

    cols = st.columns(len(results))
    for col, (model, content, elapsed) in zip(cols, results):
        with col:
            st.subheader(model)
            st.caption(f"{elapsed:.1f}s")
            st.write(content)
