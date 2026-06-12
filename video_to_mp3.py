import os
import subprocess

files = os.listdir("videos")

for file in files:
    print(file)

    tutorial_number = file.split("[")[0].split("#")[1]
    file_name = file.split("]")[0]

    output_path = f"audios/{tutorial_number}_{file_name}.mp3"

    subprocess.run([
        "ffmpeg",
        "-i",
        f"videos/{file}",
        output_path
    ], check=True)
   