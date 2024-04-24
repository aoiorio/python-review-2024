import csv
with open('/Users/atoatoatomu/Desktop/2024-programming-class/python_review/csv-analysis/titanic3.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        result_row_upper = row[2].upper()
        print(result_row_upper)