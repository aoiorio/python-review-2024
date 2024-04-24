import csv
import pprint

# Quiz 1
with open('/Users/atoatoatomu/Desktop/2024-programming-class/python_review/csv-analysis/titanic3.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        result_row_small = row[2].lower()
        print(result_row_small)

