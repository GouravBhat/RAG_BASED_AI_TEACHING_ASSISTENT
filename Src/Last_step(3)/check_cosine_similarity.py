import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

from rich.console import Console
from rich.panel import Panel
import joblib
import requests
import json


# ---------------- INIT ----------------
console = Console()
df=joblib.load('mydata.joblib')
model = SentenceTransformer("all-MiniLM-L6-v2")
def sec_to_min(seconds):
    minutes = int(seconds // 60)
    sec = int(seconds % 60)
    return f"{minutes}:{sec:02d}"



def inference_stream(prompt):
    console.print(Panel("🤖 AI Answer", style="bold green"))
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:latest",   # or deepseek-r1:1.5b
            "prompt": prompt,
            "stream": True,
            "options": {
                "temperature": 0,
                "top_p": 0.1
            }
        },
        stream=True
    )

    

    for line in r.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            token = data.get("response", "")
            print(token, end="", flush=True)
            if data.get("done", False):
                break

    
    

    

console.clear()
console.print(Panel("🎓 AI Teaching Assistant", style="bold cyan"))

question = console.input("\n[bold yellow]❓ Ask your question: [/bold yellow]")
console.print("\n[italic green]⏳ Thinking...[/italic green]\n")
question_embedding=model.encode([question])[0]
# print(np.vstack(df['embedding'].values))

similarities = cosine_similarity(np.vstack(df['embedding'].values),[question_embedding]).flatten()
top_result=similarities.argsort()[::-1][0:10]
new_df=df.loc[top_result].copy()
new_df['start']=new_df['start'].apply(sec_to_min)
new_df['end']=new_df['end'].apply(sec_to_min)

video_refs = ""
for i, row in new_df.iterrows():
    video_refs += f"Video No: {row['number']} | startTime: {row['start']} | endtime: {row['end']} | Text: {row['text']}\n"



prompt = f"""
You are an AI Teaching Assistant.

Your task is to answer the user's question ONLY using the provided video transcript data.

--------------------
USER QUESTION:
{question}
--------------------

You are given multiple video references related to the question.
Some references may be introductory, some may be continuation, and some may be the main teaching point.

--------------------
VIDEO TRANSCRIPTS:
{video_refs}
--------------------

INSTRUCTIONS (VERY IMPORTANT):
1. Analyze all the provided video transcripts carefully.
2. Identify which lecture actually INTRODUCES or TEACHES the topic.
3. Ignore references that only mention revision, continuation, or future learning.
4. Derive ONE final and most accurate conclusion.
5. Answer in ONLY ONE CLEAR SENTENCE.
6. Do NOT explain your reasoning.
7. Do NOT mention multiple lectures unless absolutely necessary.
8. Do NOT add any information that is not present in the transcripts.
9. If the exact answer cannot be concluded, say:
   "This information is not clearly stated in the provided videos."

--------------------
ANSWER FORMAT (STRICT):

Final Answer:
- Be accurate.
- Be concise but explanatory.
- Do not mention words like "chunk", "embedding", or "similarity" in the final answer.
<ONE LINE ACCURATE ANSWER ONLY Clear and well-structured explanation here>

"""


with open('prompt.txt','w')as f:
    f.write(prompt)

with open('prompt.txt','r') as f:
    prompt_final=f.read()

inference_stream(prompt_final)

# joblib.dump(prompt,'prompt.txt')

# prompt=joblib.load('prompt.txt')

# inference(prompt)


