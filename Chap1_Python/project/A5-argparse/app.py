from world_greet import greet, farewell
import argparse


def main(args):
    name = args.name if args.name else ""
    print(greet(args.lang), name)
    print(farewell(args.lang), name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("lang")
    parser.add_argument("-n", "--name", help="your name")
    args = parser.parse_args()
    print("ARGS: ", args)
    main(args)
