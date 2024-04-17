# For hanami's voice
import speech_recognition as sr
import ffmpeg
from pydub import AudioSegment
import os

def transcribe():
    # 入力
    stream_input = input("Do you want to transcribe Hanami's voice? Y/N: ")
    if stream_input == "Y":
        stream_input = "hanami.mp4"
    else:
        stream_input = input("Please input the video's path: ")

    if stream_input[-1] != "4":
        print("Please input mp4 file")
        return

    stream = ffmpeg.input(stream_input)

    # change to mp3 file
    name_to_mp3 = stream_input[:-4] + ".mp3"
    stream = ffmpeg.output(stream, name_to_mp3)
    ffmpeg.run(stream, overwrite_output=True)

    # The logic of reversing audio
    sound = AudioSegment.from_file(name_to_mp3, "mp3")
    sound_reverse = sound.reverse()
    name_to_export_reverse = name_to_mp3[:-4] + "_output" + ".mp3"
    sound_reverse.export(name_to_export_reverse, format="mp3")

    stream = ffmpeg.input(name_to_export_reverse)

    # Change to wav file from reverse audio
    name_to_wav = name_to_export_reverse[:-4] + ".wav"
    # Change the type to wav, convert name and .wav
    stream = ffmpeg.output(stream, name_to_wav)
    # Convert to wav file
    ffmpeg.run(stream, overwrite_output=True)

    # Recognize letters from wav file
    r = sr.Recognizer()

    # Convert to AudioFile?? and it defines as source
    with sr.AudioFile(name_to_wav) as source:
        audio = r.record(source)

    result = r.recognize_google(audio, language='ja-JP')


    # Remove the file created
    os.remove(name_to_export_reverse)
    os.remove(name_to_mp3)
    os.remove(name_to_wav)

    print(result)

# 🎉 Execute!
transcribe()