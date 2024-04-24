import sys

# pathの設定 (pip showで出てきた、LocationのPATHを以下に設定) Set path
sys.path.append(
    "/Users/atoatoatomu/Desktop/2024-programming-class/python_review/csv-exam/csv-examenv/lib/python3.12/site-packages"
)


from spire.xls import *
from spire.common import *

# Workbookクラスのオブジェクトを作成し、Excelファイルをロードする
# it depends on libSkiaSharp.dylib file, so you must prepare it
workbook = Workbook()
workbook.LoadFromFile("/Users/atoatoatomu/Desktop/2024-programming-class/python_review/csv-exam/excel-data.xlsx")

# ExcelファイルをPDFファイルに変換して保存する
workbook.SaveToFile("output/convert-pdf-from-csv.pdf", FileFormat.PDF)
workbook.Dispose()
