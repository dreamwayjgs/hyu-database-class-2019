def greet(lang):
    if lang == "ko":
        print("안녕 세상")
    elif lang == "es":
        print("Hola Mundo")
    else:
        print("Hello world!")


def main():
    lang = input("Input your lang code: ")
    greet(lang)


if __name__ == "__main__":
    main()
