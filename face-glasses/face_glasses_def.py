import sys

# pathの設定 (pip showで出てきた、LocationのPATHを以下に設定) Set path
sys.path.append(
    "/Users/atoatoatomu/Desktop/2024-programming-class/python_review/face-glasses/face-glasses-env/lib/python3.12/site-packages"
)
import cv2

def recognize_face(image_path):
    img = cv2.imread(image_path)

    # 正面を向いている顔を学習したカスケード分類器が保存されているパス
    cascade_path = "/Users/atoatoatomu/Downloads/haarcascade_frontalface_default.xml"

    # 学習済みモデルを読み込む
    cascade = cv2.CascadeClassifier(cascade_path)

    # 画像をグレースケールに変換
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 顔を検出する
    face_detect = cascade.detectMultiScale(img_gray)
    print(f"face_detect: {face_detect}")


    result_x = 0
    result_y = 0

    for (x,y,w,h) in face_detect:
        result_x = x
        result_y = y

    # it'll return as taple
    return result_x, result_y
