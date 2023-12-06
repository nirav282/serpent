#Set update() in Python to do union of n arrays

arrays = [[1,2,3],
          [3,4,5],
          [6,7,8]]
union_set = set()
for array in arrays:
    set_from_array = set(array)
    union_set.update(set_from_array)

print(union_set)