from argparse import ArgumentParser
from .virtualmachine import VirtualMachine
from .structs import Matrix


def main2():
    parser = ArgumentParser(
        prog="superlobster",
        description="SuperLobster",)

    parser.add_argument("filename", type=str, help="input file")
    parser.add_argument("-o", "--output", type=str, default="a.png", help="where to save output",  dest="output")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose output")
    parser.add_argument("-V", "--version", action="version", help="see current version", version="%(prog)s 0.1")

    args = parser.parse_args()
    print(args)


def main():
    img = Matrix(8, 8)

    img.set(0, 0, 1)   # no op
    img.set(1, 0, 1)   # load 1 into brain
    img.set(2, 0, 34)  # turn right
    img.set(2, 1, 47)  # right swap
    img.set(2, 2, 32)  # add
    img.set(2, 3, 77)  # print number
    img.set(2, 4, 46)  # turn left
    img.set(3, 4, 39)  # no op
    img.set(4, 4, 32)  # no op
    img.set(5, 4, 25)  # no op
    img.set(6, 4, 56)  # turn left
    img.set(6, 3, 45)  # left swap
    img.set(6, 2, 92)  # input
    img.set(6, 1, 53)  # turn left if not 0
    img.set(6, 0, 62)  # halt
    img.set(5, 1, 46)  # no op
    img.set(4, 1, 79)  # turn right
    img.set(4, 0, 48)  # turn left
    img.set(3, 0, 65)  # subtract (effective no op)

    vm = VirtualMachine(img)
    vm.run()


if __name__ == "__main__":
    main()
