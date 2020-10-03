from world_greet import greet, farewell


def main():
    lang = input("Input your lang code: ")
    print(greet(lang))
    print(farewell(lang))


if __name__ == "__main__":
    main()
