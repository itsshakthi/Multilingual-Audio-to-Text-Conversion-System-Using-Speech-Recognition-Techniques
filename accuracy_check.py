import os
from jiwer import wer

predicted_folder = r"C:\Users\shakt\OneDrive\Desktop\voice to text\data\transcripts"
reference_folder = r"C:\Users\shakt\OneDrive\Desktop\voice to text\data\reference_text"

for file in os.listdir(reference_folder):
    if file.endswith(".txt"):
        ref_path = os.path.join(reference_folder, file)
        pred_path = os.path.join(predicted_folder, file)

        if os.path.exists(pred_path):
            with open(ref_path, "r", encoding="utf-8") as f:
                reference_text = f.read()

            with open(pred_path, "r", encoding="utf-8") as f:
                predicted_text = f.read()

            error_rate = wer(reference_text, predicted_text)
            accuracy = (1 - error_rate) * 100

            print(f"{file}")
            print(f"WER: {error_rate:.2f}")
            print(f"Accuracy: {accuracy:.2f}%\n")
