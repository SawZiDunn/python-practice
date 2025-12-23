def read0():
    # with open("name.csv", "r") as file:
    #     lines = file.readlines()  # lines is a list
    # #  readlines() read all the lines in a file and keep them in a list
    #
    # for line in lines:
    #     print(line.rstrip())  # rstrip() is same with strip() except for being right only

    with open("name.csv") as file:  # read method can be omitted
        for line in sorted(file, reverse=True):  # file can be sorted
            print(line.rstrip())


def read1():
    count = 0
    total = 0
    file = input("Type the file name: ")
    opened_file = open(file, "r")


    # only for files with one number in each line(can have multiple lines) eg. "a.txt"

    for line in opened_file:  # open_file.readlines() can be used
        count = count + 1
        total += int(line)
    opened_file.close()
    print("The average is", round(total / count, 2))


def read2():
    count = 0
    total = 0
    filepath = input("Type your file name: ")
    file = open(filepath)
    line = file.readline()  # only reads one line at a time

    while line != "":  # or while line: # while there's a line
        count = count + 1
        total = total + eval(line.strip())  # strip() is not necessary
        line = file.readline() # read the next line
    print("The average is", total / count)


def read3():
    total = 0
    count = 0
    filename = input("Type your file name")
    file = open(filename, "r")
    line = file.readline()

    # for files with multiple numbers in one line separated by something(can have multiple lines)
    # eg. "b.txt"
    # also works for 'a.txt'

    while line != "":
        for x in line.split(","):
            total = total + eval(x)
            count = count + 1
        line = file.readline()
    print(total)
    print("The average number is", total / count)
    
    
if __name__ == "__main__":
    read1()

