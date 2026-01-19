import os
import speech_recognition as sr

# ====== LANGUAGE SETTING ======
# Change this when needed
LANGUAGE_CODE = "ta-IN"   # examples: en-IN, hi-IN, ta-IN, te-IN

# ====== PATHS ======
input_folder = r"C:\Users\shakt\OneDrive\Desktop\voice to text\data\processed_audio"
output_folder = r"C:\Users\shakt\OneDrive\Desktop\voice to text\data\transcripts"

os.makedirs(output_folder, exist_ok=True)

recognizer = sr.Recognizer()

for file in os.listdir(input_folder):
    if file.endswith(".wav"):
        wav_path = os.path.join(input_folder, file)

        # language-specific output file
        txt_filename = file.replace(".wav", f"_{LANGUAGE_CODE}.txt")
        txt_path = os.path.join(output_folder, txt_filename)

        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data, language=LANGUAGE_CODE)
                with open(txt_path, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"Transcribed {file} → {txt_filename}")
            except sr.UnknownValueError:
                print(f"Could not understand {file}")
            except sr.RequestError as e:
                print(f"API error for {file}: {e}")
