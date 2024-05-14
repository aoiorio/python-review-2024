import sys
sys.path.append("/Users/atoatoatomu/Desktop/2024-programming-class/python_review/csv-train/csv_train_env/lib/python3.12/site-packages")
import pandas as pd #pandasをpdとしてインポート

#データをdfに読み込み。pandasをpdとして利用。
df = pd.read_csv("/Users/atoatoatomu/Desktop/2024-programming-class/python_review/csv-train/train.csv")

# Show first 5 rows
print(df.head()) #最初の5行を表示

