import math
for i in range(101):
    formula1 = 1 / math.sqrt(5)
    formula2 = ((1 + math.sqrt(5)) / 2) ** i
    formula3 = ((1 - math.sqrt(5)) / 2) ** i
    result = formula1 * (formula2 - formula3)
    print(int(result))

# print(math.sqrt(5) / 1)

"""
1 + 1 = 2 (1 * 2) + (0)
2 + 3 = 5 (2 * 2) + (1)
3 + 5 = 8 (3 * 2) + (2)
5 + 8 = 13 (5 * 2) + (3)
13 + 8 = 21 (8 * 2) + (5)
21 + 13 = 34 (13 * 2) + (8)
34 + 21 = 55 (21 * 2) + (13)
"""

# for i in range(101):
#     for j in range(50):
#         print(i + j)

list = []

for i in range(101):
    try:
        if i == 0:
            print(1)
            continue
        list.append(i)
        print(list[i] - list[i - 1])
    except IndexError:
        break