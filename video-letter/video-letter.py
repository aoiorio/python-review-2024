import os
import tkinter as tk
from tkinter import filedialog
import speech_recognition as sr
import time
import ffmpeg
from pydub import AudioSegment

print("音声の文字起こしプログラムです")
print("")
print("【対象フォーマット】")
print("動画・・・mp4 avi mov mkv wmv flv")
print("音声・・・wav mp3 flac ogg aac aiff aif")
print("")
print("動画または音声を指定してください")
print("")

#文字起こし対象の動画または音声の指定
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title="動画または音声ファイルを選択してください")
show_file_name = os.path.basename(file_path)

print("選択したファイル名：", show_file_name)
print("")
print("動画の音声を分析しています・・・")
print("")

#ファイル名から拡張子を返す式
extension = file_path.split('.')[-1].lower()

#処理対象の拡張子かどうかを判別
supported_extensions = ['mp4', 'avi', 'mov', 'mkv', 'wmv', 'flv', 'wav', 'mp3', 'flac', 'ogg', 'aac', 'aiff', 'aif']

#対応外の場合はプログラムを終了する
if extension not in supported_extensions:
    print("サポートされていないファイル形式です。")
    print("")
    time.sleep(5)
    exit(1)

print("選択したファイル名：",show_file_name)
print("")
print("文字起こし処理中です・・・")
print("")

r = sr.Recognizer()

try:
    #拡張子がwav以外であれば「output.wav」として一時ファイルを出力する
    #ffmpegで音声を抜き出し、wavに変換する
    if extension in supported_extensions:
        if extension != 'wav':
            output_wav_file = "output.wav"

            ffmpeg.input(file_path).output(output_wav_file, acodec='pcm_s16le', ac=1, ar='16000').overwrite_output().run()
            wav_file_path = output_wav_file

    #wavの文字起こし処理
    with sr.AudioFile(wav_file_path) as source:
        audio = r.record(source)
        transcript = r.recognize_google(audio, language='ja-JP')

    #テキスト出力処理
    text_file_name = f"{show_file_name.split('.')[0]}.txt"
    text_file_path = os.path.join(os.path.dirname(os.path.abspath(file_path)), text_file_name)
    with open(text_file_path, 'w', encoding='utf-8') as f:
        f.write(transcript)

    # output.wavを削除
    os.remove(output_wav_file)


    print("")
    print(transcript)
    print("")
    print("上記の通り、認識しました")
    print("出力済テキストデータは以下に保存されています")
    print("")
    print(text_file_path)
    print("")
    print("60秒後にプログラムを閉じます")
    print("または右上の×で閉じてください")
    time.sleep(60)

except Exception as error:
    print("以下のエラーが発生しました:")
    print(error)
    time.sleep(5)