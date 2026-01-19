import os
import soundfile as sf

input_folder = r"C:\Users\shakt\OneDrive\Desktop\voice to text\data\raw_audio"
output_folder = r"C:\Users\shakt\OneDrive\Desktop\voice to text\data\processed_audio"

for file in os.listdir(input_folder):
    if file.endswith(".flac"):
        flac_path = os.path.join(input_folder, file)
        wav_path = os.path.join(output_folder, file.replace(".flac", ".wav"))
        data, samplerate = sf.read(flac_path)
        sf.write(wav_path, data, samplerate)
        print(f"Converted {file} → {wav_path}")
