from argparse import ArgumentParser

from .interpreter import *


def main():
	parser = ArgumentParser(
		prog="superlobster",
		description="SuperLobster",)

	parser.add_argument("filename", type=str, help="input file")
	parser.add_argument("-o", "--output", type=str, default="a.png", help="where to save output",  dest="output")
	parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose output")
	parser.add_argument("-V", "--version", action="version", help="see current version", version="%(prog)s 0.1")

	args = parser.parse_args()
	print(args)

if __name__ == "__main__":
	main()