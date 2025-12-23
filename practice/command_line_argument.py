import sys
import argparse


def sample0():
    # If you pass an argument in double quotes, python will take it as one argument

    if len(sys.argv) != 2:
        sys.exit("Too many or too few arguments...")  # exit by printing the given

    print(f"Hello, my name is {sys.argv[1]}.")

    # try:
    #     print(f"Hello, my name is {sys.argv[1]}.")
    # except Exception as err:  # IndexError
    #     print(err)


def sample1():
    parser = argparse.ArgumentParser(description="Meow like a cat!")
    parser.add_argument("-n", default=1, help="number of times to meow", type=int)
    args = parser.parse_args()

    for _ in range(args.n):  # args.n is the argument after '-n'
        print("Meow!")
    

if __name__ == '__main__':
    sample1()
