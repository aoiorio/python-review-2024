import cv2
# 顔を検出する画像のパス
img_path = input()

# 画像を読み込む
img = cv2.imread(img_path)

# 正面を向いている顔を学習したカスケード分類器が保存されているパス
cascade_path = "/Users/atoatoatomu/Downloads/haarcascade_frontalface_default.xml"

# 学習済みモデルを読み込む
cascade = cv2.CascadeClassifier(cascade_path)

# 画像をグレースケールに変換
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 顔を検出する
face_detect = cascade.detectMultiScale(img_gray)

# 検出した顔を赤く囲む
img_copy = img.copy()

for (x,y,w,h) in face_detect:
    cv2.rectangle(img_copy, (x, y), (x+w, y+h), color=(0, 0, 255), thickness=3)

# 顔検出後の画像表示
cv2.imwrite("/Users/atoatoatomu/Downloads/hito_shikaku.jpg", img_copy)
print("end!")