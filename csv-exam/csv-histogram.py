import sys

# pathの設定 (pip showで出てきた、LocationのPATHを以下に設定) Set path
sys.path.append(
    "/Users/atoatoatomu/Desktop/2024-programming-class/python_review/csv-exam/csv-examenv/lib/python3.12/site-packages"
)


import pandas as pd
import matplotlib.pyplot as plt
import math
# 1. ライブラリのインポート
import pandas as pd
# Excelファイルの読み込み
data = pd.read_excel('/Users/atoatoatomu/Desktop/2024-programming-class/python_review/csv-exam/excel-data.xlsx', 'Sheet1', index_col=None)

# CSV形式で出力
data.to_csv('csv-exam-data.csv')

# 2. CSVファイルをPandas DataFrameに読み込む
# 以下の例では、"data.csv"というCSVファイルを読み込んでいます。適切なファイルパスを指定してください。
df = pd.read_csv("/Users/atoatoatomu/Desktop/2024-programming-class/python_review/csv-exam/csv-exam-data.csv")

#3データサイズ、bin数を求める
datasize = df.shape[0]
bin_number = round(math.sqrt(datasize))


# 4. Create histogram
# ヒストグラムを描画する前に、適切な列（データセット内の特定の列）を選択します。

# Create histogram from math score (you can change this value's name)
plt.hist(df["math score"], bins=bin_number,edgecolor = 'black')  # "value"列のデータを使用し、10つのビンでヒストグラムを作成

# ヒストグラムのタイトルやラベルを設定することもできます
plt.title("Histogram of Values")
plt.xlabel("Scores")
plt.ylabel("Number of people")

# ヒストグラムを表示
plt.show()