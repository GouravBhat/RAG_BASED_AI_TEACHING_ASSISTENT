import whisper
import os
import json
FOLDER_PATH = "speech"
model = whisper.load_model("large-v2")
video_extensions = (".mp4", ".mkv", ".avi", ".mov",".mp3")
for file in os.listdir(FOLDER_PATH):
    print(file) #47. DOM + Modern JS - Class I [HD].mp4
    if file.lower().endswith(video_extensions):
      vedio_number=file.split(".")[0]
      json_file = file.split(".")[0] + ".json"
      file_path = os.path.join(FOLDER_PATH, file)
      result = model.transcribe(file_path,language='hi',task='translate')
      chunks=[]
      for chunk in result['segments']:
        chunks.append({"number":vedio_number,"start":chunk['start'],"text":chunk['text'],"end":chunk['end']})
      chunks_with_metadata={
          "chunks":chunks,
          "text":result['text']
      }
      with open(f"output/{json_file}","w")as f:
        json.dump(chunks_with_metadata,f)    
