# def unpacking(*value):
#     value_sum = 0
#     for i in data_structure:
#         if i == None:
#             continue
#         if isinstance(i, (int, float)):
#             value_sum += i
#         if isinstance(i, str):
#             value_sum += len(i)
#         if isinstance(i, (list, tuple, set)):
#              *i
#             # if isinstance(i, dict):
#             #     value += i.items()
#     return value_sum

def unpacking(value):
    value_sum = 0
    for i in value:
        # if i == value:
        #     return value_sum
        if isinstance(i, (int, float)):
            value_sum += i
        elif isinstance(i, str):
            value_sum += len(i)
        elif isinstance(i, (list, tuple, set)):
            unpacking(i)
        elif isinstance(i, dict):
            value += i.items()
    return value_sum

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  # (6, {'cube': 7, 'drum': 8}),
  # "Hello",
  # ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(unpacking(data_structure))





# data_structure = [(
#   [1, 2, 3],
#   # {'a': 4, 'b': 5},
#   # (6, {'cube': 7, 'drum': 8}),
#   "Hello"
#   # ((), [{(2, 'Urban', ('Urban2', 35))}])
# )]



        # Опыты

# q = {'a': 4, 'b': 5}
# q_ = [*q]
# q__ = [*q.values()]
# print(q_)
# print(q__[1])
#
# list__ = [1, 2, 3]
# x1, x2, x3 = list__
# print(x1)
#
# tuple__ = (4, 5, 6)
# x4, x5, x6 = tuple__
# print(x4)
#
# list___ = ['urban', 'Olga']
# list___2 = []
# for i in list___:
#     list___2.append(len(i))
# print(list___2)

# def proba(*mnogo):
#     print(mnogo)
#
# proba(2, 3)

# def slojenie(list_66):
#     global x2
#     x1 = list_66[0]
#     x2 = list_66[1]
#     y = x1 + delenie(x1)
#     print(y)
#     return y
#
# def delenie(list_66):
#     x3 = x2 / 2
#     return x3
#
# x2 = 0
# list_66 = [2, 4, 6]
# slojenie(list_66)

# list_77 = (3, 4, 5)
# list_88 = sum(list_77)
# print(list_88)