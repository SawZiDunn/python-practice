def main():
    n = int(input("What's n?: "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "Sheep" * i  # this returns every time

main()


