
try:
    sen = "hello"
    print(sen / 3)
except TypeError:
    print("Type error occurred")

test_file = open("/Users/atoatoatomu/Desktop/2024-programming-class/python_review/2024-4-24/text.txt", "r")
test_text = test_file.read()
print(test_text)
test_file.close()

with open('/Users/atoatoatomu/Desktop/2024-programming-class/python_review/2024-4-24/text.txt', 'r') as test_file:
    print(test_file.read())