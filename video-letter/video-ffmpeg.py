import whisper
import json

model = whisper.load_model("small") #モデルの指定
result = model.transcribe("/Users/atoatoatomu/Downloads/hanami.mp4", verbose=True, fp16=False, language="ja") #ファイルの指定
print(result['text'])

f = open('transcription.txt', 'w', encoding='UTF-8')
f.write(json.dumps(result['text'], sort_keys=True, indent=4, ensure_ascii=False))
f.close()