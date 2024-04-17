# What were you doing!!!!!!
save_dict_list = [[0, 1]]
result = {}

for i in range(1, 100):
    # if len(save_dict_list) >= 6:
    #     break
    if i % 3 == 0:
        # print(save_dict_list[i - 1])
        # print(i - 4)
        save_dict_list.append([i, save_dict_list[i - 1][1] + i])
    else:
        # print("this is i -1 i !!" + str(save_dict_list[i - 1][1] + i))
        # print(save_dict_list[i - 1])
        save_dict_list.append([i, sum(save_dict_list[i - 1])])
        # print(3)
    # これだとi - 1の値にkeyがなってしまう
    # save_dict[i] = save_dict[i - 1]
    # print(save_dict_list[i -1])
    # save_dict_list.append([i, save_dict_list[i - 1][1] + i])
    # save_dict_list.append([i, sum(save_dict_list[i - 1])])

# print(save_dict_list)
    # print(len(save_dict))

# for k,v in save_dict_list.items():
#     print(v)
# 前のlist[i -1][1]
"""
辞書で、まとめる
前の値を辞書にkeyをiで格納して格納してあるkeyの値を取得、そのkeyとiを足す
そして、keyとiを足したものを辞書の値として格納する？？
いや、lenで取り出した方が良くないか？？

"""

dict_test = {0: 1, 1: 1, 2: 3, 3: 5, 4: 8}
dict_test_list = [{0: 1}, {1: 1}, {2: 3}, {3: 5}, {4: 8}]
print(len(dict_test))

"""
3で割れるところは、前の値(save_dict_list[i - 1][1]とiのsumで
その他は、前のsave_dict_list[i - 1]のsumである？
"""

li = []
result_list = []

# for i in range(0, 100):
#     li.append(i)
#     result_list.append(i + li[i - 1])

# print(result_list)

# The answer!!!!!!! Simple and stylish!!!!
a, b = 0, 1
for i in range(99):
    # この時はまだ、bが前の値(a + b)であるのでそれを使って書いている！！！！
    # a にbを代入し、bにまだ残っている値 a + bを代入する
    a, b = b, a+b
    # bにはa + bが入っているので上からこの作業を繰り返していく。
    print(a, b)

    # print(b)