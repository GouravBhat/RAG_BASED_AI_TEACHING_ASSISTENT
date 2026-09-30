import os
import json
import math
n=5
for file in os.listdir('output'):
    if file.endswith('.json'):
        file_path=os.path.join('output',file)
        with open(file_path,'r')as f:
            data=json.load(f)
            new_chunks=[]
            num_chunks=len(data['chunks'])
            print(num_chunks)
            num_groups=math.ceil(num_chunks/n)
            print(num_groups)
            for i in range(num_groups):
                start_index=i*n
                end_index=min((i+1)*n,num_chunks)

                chunk_group=data['chunks'][start_index:end_index]

                new_chunks.append({
                    "number":chunk_group[0]['number'],
                    "start":chunk_group[0]['start'],
                    "end":chunk_group[-1]['end'],
                    'text':" ".join(c['text'] for c in chunk_group)
                })
            chunks_with_metadata={
                "chunks":new_chunks,
                "text":data['text']
            }
            with open(f"newChunks/{file}","w")as f:
                json.dump(chunks_with_metadata,f)  
            
          
                
        