import sys

# pathの設定 (pip showで出てきた、LocationのPATHを以下に設定) Set path
sys.path.append(
    "/Users/atoatoatomu/Desktop/2024-programming-class/python_review/photo/photoenv/lib/python3.11/site-packages"
)
import cv2
img_path = input()

def recognize_face(image_path):
    img = cv2.imread(img_path)

    # 顔を検出する画像のパス

    # 画像を読み込む

    # 正面を向いている顔を学習したカスケード分類器が保存されているパス
    cascade_path = "/Users/atoatoatomu/Downloads/haarcascade_frontalface_default.xml"

    # 学習済みモデルを読み込む
    cascade = cv2.CascadeClassifier(cascade_path)

    # 画像をグレースケールに変換
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 顔を検出する
    face_detect = cascade.detectMultiScale(img_gray)
    print(f"face_detect: {face_detect}")

    # 検出した顔を赤く囲む
    img_copy = img.copy()

    for (x,y,w,h) in face_detect:
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), color=(0, 0, 255), thickness=3)

    # 顔検出後の画像表示
    cv2.imwrite("/Users/atoatoatomu/Downloads/hito_shikaku.jpg", img_copy)
    return {"face_detect": face_detect}

recognize_face(img_path)