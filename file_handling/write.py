import csv


def write0():
    name = input("Enter your name: ")

    # file = open("name.csv", "a")

    with open("name.csv", "a") as file:
        file.write(name + "\n")
        
    # file.close()  # not necessary if we use 'with'


def write1():
    name = input("What's your name?: ")
    clan = input("What's your clan?: ")
    with open("name.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, clan])


def write2():
    name = input("What's your name?: ")
    clan = input("What's your clan?: ")
    with open("name.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "clan"])
        writer.writerow({"name": name, "clan": clan})


write2()
