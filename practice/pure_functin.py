list_sample = [1, 2, 3, 4, 5]

def append_list(array, item):
    nl = array.copy()
    nl.append(item)
    return nl

new_list = append_list(list_sample, 6)
print(list_sample)
print(new_list)

# if the functin does not change the data from global scope (outside the function),
# it is called a pure function