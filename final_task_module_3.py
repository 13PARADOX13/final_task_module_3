def unpacking(*value):
    value_sum = 0
    for i in value:
        if i == None:
            continue
        elif isinstance(i, (int, float)):
            value_sum += i
        elif isinstance(i, str):
            value_sum += len(i)
        elif isinstance(i, (list, tuple, set)):
            value_sum += unpacking(*i)
        elif isinstance(i, dict):
            value_sum += unpacking(*i.items())
    return value_sum

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(unpacking(data_structure))
