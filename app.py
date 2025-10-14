import os
from pipeline import audio, stt, summarize, quiz, utils, concept_map

video_file = "lecture.mp4"   # path to your lecture video
out_dir = "outputs"
utils.ensure_dir(out_dir)

# 1️⃣ Extract audio
audio_file = os.path.join(out_dir, "lecture.wav")
audio.extract_audio(video_file, audio_file)

# 2️⃣ Transcribe
print("Transcribing...")
text = stt.transcribe_audio(audio_file)
utils.save_text(os.path.join(out_dir, "transcript.txt"), text)

# 3️⃣ Summarize notes
print("Summarizing...")
notes = summarize.summarize_text(text)
utils.save_text(os.path.join(out_dir, "notes.txt"), notes)

# 4️⃣ Generate contextual quiz
print("Generating contextual quiz...")
quiz_list = quiz.generate_contextual_quiz(notes, num_questions=5)
with open(os.path.join(out_dir, "quiz.txt"), "w", encoding="utf-8") as f:
   for i, q in enumerate(quiz_list, 1):
    f.write(f"Q{i}: {q['question']}\n"
            f"A{i}: {q['answer']}\n"
            f"Context: {q['context']}\n\n")


# 5️⃣ Generate concept map
print("Generating concept map...")
concept_map_file = os.path.join(out_dir, "concept_map.png")
concept_map.build_concept_map(notes, concept_map_file)

print("✅ Done! Check the outputs folder for notes, quiz, and concept map.")
