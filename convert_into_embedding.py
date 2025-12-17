from sentence_transformers import SentenceTransformer
import os
import json
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity
# # 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")
FOLDER_NAME="newChunks"
# def conversion_text_to_vectors(text):
#     sentences=text
#     embeddings=model.encode(sentences)
#     return embeddings




extension=(".json")
my_dict=[]
chunk_id=0
for file in os.listdir(FOLDER_NAME):

    if file.lower().endswith(extension):
        folder_path=os.path.join(FOLDER_NAME,file)
        with open(folder_path,'r')as f:
            data=json.load(f)
        print(file)
        embedding=model.encode([c['text'] for c in data['chunks']]) 
        
        for i,chunk in enumerate(data['chunks']):
            chunk['chunk_id']=chunk_id
            chunk['embedding']=embedding[i]
            chunk_id += 1
            my_dict.append(chunk)
        
            
df=pd.DataFrame.from_records(my_dict) 
# print(df['embedding'])
print(df)
joblib.dump(df,'mydata.joblib')





