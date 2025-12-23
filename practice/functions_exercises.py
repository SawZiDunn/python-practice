def find_largest():
    lists = [100, 5, 6, 4, 7, 8, 9, 5, 4, 1, 2, 5, 8, 7, 4, 58, 9, 59]
    largest_num = 0
    for i in range(len(lists)):
        if lists[i] >= largest_num:
            largest_num = lists[i]
    print(f"The largest number in the list is {largest_num}.")


def find_smallest():
    lists = [6, 4, 7, 6, 5, 5, 4, 1, -5, 2, 5, 8, 7, 4, 58, 9]
    smallest_num = lists[0]

    for i in lists:
        if i < smallest_num:
            smallest_num = i
    print(f"The smallest number in the list is {smallest_num}.")


def duplication_remove():
    lists = [6, 4, 7, 6, 5, 5, 4, 4, 4, 5, 6, 4, 5]
    new_lists = []

    for num in lists:
        if num not in new_lists:
            new_lists.append(num)
    print(new_lists)


def num_interpret():
    x = input("Input your phone number:")
    y = ""
    digits = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
    }

    for i in x:
        y += digits.get(i, "!") + " "
    print(y)


def triangle_pattern():
    nrow = eval(input("enter number of rows: "))
    for i in range(nrow):
        for j in range(i+1):
            print(j+1, end=" ")
        print("\n")


def printer():
    a = 10
    b = 50
    c = 1.2354658

    print(f"{a} is less than {b}")
    print("The value of c is %.2f." % c)

    print("{1} is greater than {0}".format(a, b))

    print("Hello {name}, Welcome to {an} {num}.".format(name="ZiDunn", an="Golden Land", num=37))

    


triangle_pattern()