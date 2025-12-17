import os
import subprocess

FOLDER_PATH='vedios'
Audio_folder='Audio'

video_extensions = (".mp4", ".mkv", ".avi", ".mov", ".flv", ".webm")

for file in os.listdir(FOLDER_PATH):
    print(file) #47. DOM + Modern JS - Class I [HD].mp4
    if file.lower().endswith(video_extensions):
        # video_path = os.path.join(FOLDER_PATH,file)
        # print(video_path)
        mp3_file = file.split(".")[0] + ".mp3"
        
        print(mp3_file)
        

        command = [
            "ffmpeg",
            "-i", f"{FOLDER_PATH}\{file}",
            f"{Audio_folder}\{mp3_file}"
        ]

        subprocess.run(command)

        print(f"✅ Converted: {file} → {mp3_file}")

print("🎉 All videos converted successfully")
