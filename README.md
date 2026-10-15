# 03 – Ollama Model Arena

Send one prompt to all of your local models at once and compare their answers + response time side by side — useful since you're already running three different models for different jobs.

## Setup
```bash
pip install -r requirements.txt
```

## Usage
```bash
streamlit run app.py
```
Edit the `MODELS` list at the top of `app.py` if your exact Ollama tags differ (check with `ollama list`).

## How it works
Uses a thread pool to query all configured models concurrently (so you're not waiting for them one at a time), then renders each model's answer in its own column along with how long it took — handy for deciding which of your three models is the right default for a given kind of task.
