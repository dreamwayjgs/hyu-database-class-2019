a = 1
b = 2
c = 3


class Human:
    name: str
    age: int

    def __init__(self, name, age) -> None:  # 생성자, constructor
        self.name = name
        self.age = age


lee = Human("Lee", 10)

print(lee)