## ✏️ How does it work?
- If you execute video-letter.py file, you can transcribe from videos.

- video-letter-own.py file is for transcribing from only Hanami's voice. Because the video will reverse and it'll be texts.

- I recommend you to use video-letter-own.py

## 😈 The logic of video-letter-own.py
- This code can convert to wav file from mp4.
```python
import ffmpeg

# Input the path to video
stream = ffmpeg.input("test.mp4")

# Choose file name to convert to wav file
stream = ffmpeg.output(stream, "test.wav")

# Execute (Change to wav file)
ffmpeg.run(stream)
```

<br>

- You can convert to mp3 file from mp4 as well.
```python
import ffmpeg

# Input the video path
stream = ffmpeg.input("test.mp4")

# Choose file name to convert to mp3 file
stream = ffmpeg.output(stream, "test.mp3")

# Execute (Change to mp3 file)
ffmpeg.run(stream)
```

<br>

- And I programed for reversing video's voice. The code is here.
``` python
# Input the audio file
sound = AudioSegment.from_file("test.mp3", "mp3")

# Reverse
reverse_sound = sound.reverse()
```

<br>

- You can transcribe easily by using SpeechRecognize

``` python
import speech_recognition as sr

# Recognize letters from wav file
r = sr.Recognizer()

# Convert to AudioFile?? and it defines as source
with sr.AudioFile('test.wav') as source:
    audio = r.record(source)

# Recognize audio
result = r.recognize_google(audio, language='ja-JP')

print(result)
```

<br>

- **🐸 The logic is like this.**
1. Input video's path (This video must be a mp4 file)
2. Change to mp3 file for reversing
3. Reverse the mp3
4. Change to wav file for transcribing
5. Transcribe
6. Remove the files that the code made