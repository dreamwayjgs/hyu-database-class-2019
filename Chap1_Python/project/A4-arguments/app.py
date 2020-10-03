from world_greet import greet, farewell
import sys


def main(argv):
    print("Command line arguments: ", argv)
    lang = argv[1] if len(argv) > 1 else "en"
    print(greet(lang))
    print(farewell(lang))


if __name__ == "__main__":
    main(sys.argv)
