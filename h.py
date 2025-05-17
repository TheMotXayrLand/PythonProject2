# === Класс Hello_world и наследник Hi ===

class Hello_world:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"

    def __init__(self):
        self.world = "World"
        self._world = "_World"
        self.__world = "__World"

    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self._Hello_world__hello)  # доступ к приватному полю
        print(self.world)
        print(self._world)
        print(self.__world)  # доступ в пределах класса


class Hi(Hello_world):
    def hi_print(self):
        print(self.hello)
        print(self.world)
        print(self._hello)
        print(self._world)
        print(self._Hello_world__hello)
        print(self._Hello_world__world)


hello = Hello_world()
hello.printer()

hi = Hi()
hi.hi_print()

# === Классы Hello и Hello_World с наследованием ===

class Hello:
    def __init__(self):
        print("Hello!")


class Hello_World(Hello):
    def __init__(self):
        super().__init__()
        print("World!")


hello_world = Hello_World()

# === Наследование Grandparent → Parent → Child ===

class Grandparent:
    def about(self):
        print("I am GrandParent")

    def about_myself(self):
        print("I am Grandparent")


class Parent(Grandparent):
    def about_myself(self):
        print("I am Parent")


class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()


nick = Child()

# === Множественное наследование: SmartPhone от Computer и Display ===

class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 128


class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "4k"


class SmartPhone(Computer, Display):
    def print_info(self):
        print(self.model)
        print(self.resolution)
        print(self.memory)


iphone = SmartPhone(model="POCO")
iphone.print_info()

# === Обработка исключений: ZeroDivisionError и NameError ===

try:
    print("start code")
    # print(dfgh)  # NameError, закомментировано
    print(10 / 0)
    print("No errors")
except NameError:
    print("NAME ERROR!!!")
except ZeroDivisionError:
    print("ZeroDivision ERROR!!!")

print("after capsule")

# === Обработка исключений с else и finally ===

try:
    print("start")
    # print(start)  # NameError, закомментировано
    print("No errors")
except (SyntaxError, NameError) as error:
    print(error)
else:
    print("I am ELSE")
finally:
    print("Finally code")

# === Проверка типа с raise TypeError ===

def checker(var_1):
    if type(var_1) != str:
        raise TypeError(f"Sorry, we can’t work with {type(var_1)}, we need class str")
    else:
        print(var_1)


first_var = 10
try:
    checker(first_var)
except Exception as e:
    print("не той тип даних:", e)

# === Пользовательское исключение BuildingEror ===

class BuildingEror(Exception):
    def __str__(self):
        return "With so much material the house cannot be built!"


def check_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        print("enough material")
    else:
        raise BuildingEror()


materials = 170
check_material(materials, 150)

