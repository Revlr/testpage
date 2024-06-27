import os
import subprocess

# def convert_files_in_directory(directory):
#     for filename in os.listdir(directory):
#         if filename.endswith(".wav"):
#             input_file = os.path.join(directory, filename)
#             output_file = os.path.join(directory,"../docs/audio", filename)
#             convert_to_mp3(input_file, output_file)

def convert_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            input_file = os.path.join(directory, filename)
            output_file = os.path.join(directory,"../docs/audio", filename)
            convert_to_mp3(input_file, output_file)

def convert_to_mp3(input_file, output_file):
    command = [
        'ffmpeg',
        '-i', input_file,
        # '-ar', '44100',
        # '-ac', '2',
        # '-sample_fmt', 's16',
        '-b:a', '192k',
        output_file
    ]
    try:
        subprocess.run(command, check=True)
        print(f"Converted {input_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert {input_file}: {e}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    convert_files_in_directory(current_directory)
