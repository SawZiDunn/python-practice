def add(x, lst=None):
    #
    # if lst is None:
    #     lst = []
    
    if x not in lst:
        lst.append(x)
    return lst

def main():
    y = add(3)
    print(y) # [3]
    z = add(2)
    print(z) # [3, 2]
    x = add(3, [1, 2])
    print(x) # [1, 2, 3]

main()