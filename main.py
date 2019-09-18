from sys import stdin
from input_parser import InputParser
from mower_controller import MowerController
from argparse import ArgumentParser


def get_input():
    argparser = ArgumentParser(
        prog='mowers',
        description='moves mowers on a lawn',
    )
    argparser.add_argument('input_file', nargs='?')
    args = argparser.parse_args()
    if args.input_file:
        return open(args.input_file)
    else:
        return stdin


def main():
    input_file = get_input()
    parser = InputParser(input_file)
    lawn, mowers = parser.parse()
    controller = MowerController(lawn, mowers)
    for m in mowers:
        print(m)


if __name__ == "__main__":
    main()
