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
    img = Matrix(5, 1)
    img.set(0, 0, 47)
    img.set(1, 0, 2)
    img.set(2, 0, 11)

    vm = VirtualMachine(img)
    vm.run()


if __name__ == "__main__":
    main()
