import sys

# pathの設定 (pip showで出てきた、LocationのPATHを以下に設定) Set path
sys.path.append(
    "/Users/atoatoatomu/Desktop/2024-programming-class/python_review/csv-exam/csv-examenv/lib/python3.12/site-packages"
)

import pandas as pd
import openpyxl


csv_path = "/Users/atoatoatomu/Downloads/exams.csv"

# CSVファイルの読み込み
data = pd.read_csv(csv_path)

# Excel形式で出力
data.to_excel("excel-data.xlsx")

# wb = openpyxl.load_workbook("/Users/atoatoatomu/Desktop/2024-programming-class/python_review/csv-exam/excel-data.xlsx")
excel_data_wb = openpyxl.load_workbook("/Users/atoatoatomu/Desktop/2024-programming-class/python_review/csv-exam/excel-data.xlsx")

def insert_col(wb, new_file_name):
    ws = wb["Sheet1"]
    ws.insert_cols(7)
    wb.save(new_file_name)

def rename_col(previous_file_name, new_file_name, new_col_name):
    df = pd.read_excel(previous_file_name)

    #▼列名の変更
    df = df.rename(columns = {'Unnamed: 6' : new_col_name})

    #▼書き出し
    df.to_excel(new_file_name, index = None)

# task 1
def insert_average():

    # insert col
    insert_col(excel_data_wb, "after-insert-average-col.xlsx")

    # rename col
    rename_col("/Users/atoatoatomu/Desktop/2024-programming-class/python_review/csv-exam/after-insert-average-col.xlsx", "after-rename-average.xlsx", "Average of points")


insert_average()

# additional task 1
def calculate_all_points(xlsx_path):
    wb = openpyxl.load_workbook(xlsx_path)
    ws = wb["Sheet1"]

    insert_col(wb, "after-insert-sum-col.xlsx")
    rename_col("/Users/atoatoatomu/Desktop/2024-programming-class/python_review/csv-exam/after-insert-sum-col.xlsx", "after-rename-and-insert-sum.xlsx", "Sum")

    exam_list = []
    header_cells = None

    for row in ws.rows:
        if row[0].row == 1:
            # １行目
            header_cells = row
            # This code can have a name of a specific row
            # print(header_cells[1].value)
        else:
            # ２行目以降
            row_dic = {}
            # セルの値を「key-value」で登録
            # zip() is a built-in function that allows you to aggregate elements from multiple iterables into a single iterable
            # it loops together in parallel
            for k, v in zip(header_cells, row):
                row_dic[k.value] = v.value
            exam_list.append(row_dic)

    for exam in exam_list:
        total_score = exam["math score"] + exam["reading score"] + exam["writing score"]
        exam["total_score"] = total_score

    # for manipulating new sheet (after inserting and renaming sum col)
    sum_wb = openpyxl.load_workbook("/Users/atoatoatomu/Desktop/2024-programming-class/python_review/csv-exam/after-rename-and-insert-sum.xlsx")
    sheet = sum_wb.active

    # add sum value into G column
    for i in range(len(exam_list)):
        sheet_index = i + 2
        sheet['G' + str(sheet_index)] = exam_list[i]["total_score"]
    sum_wb.save('after-calculate-sum.xlsx')


calculate_all_points("/Users/atoatoatomu/Desktop/2024-programming-class/python_review/csv-exam/excel-data.xlsx")

