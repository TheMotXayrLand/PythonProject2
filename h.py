# === Клас Hello_world і спадкоємець Hi ===
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
        print(self._Hello_world__hello)
        print(self.world)
        print(self._world)
        print(self.__world)


class Hi(Hello_world):
    def hi_print(self):
        print(self.hello)
        print(self.world)
        print(self._hello)
        print(self._world)
        print(self._Hello_world__hello)
        print(self._Hello_world__world)


# === Класи Hello і Hello_World ===
class Hello:
    def __init__(self):
        print("Hello!")


class Hello_World(Hello):
    def __init__(self):
        super().__init__()
        print("World!")


# === Grandparent → Parent → Child ===
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


# === Множинне успадкування ===
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


# === Обробка виключень ===
def exception_demo():
    try:
        print("start code")
        print(10 / 0)
    except NameError:
        print("NAME ERROR!!!")
    except ZeroDivisionError:
        print("ZeroDivision ERROR!!!")
    print("after capsule")

    try:
        print("start")
        print("No errors")
    except (SyntaxError, NameError) as error:
        print(error)
    else:
        print("I am ELSE")
    finally:
        print("Finally code")

    def checker(var_1):
        if type(var_1) != str:
            raise TypeError(f"Sorry, we can’t work with {type(var_1)}, we need class str")
        else:
            print(var_1)

    try:
        checker(10)
    except Exception as e:
        print("не той тип даних:", e)

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


# === Завдання 1: словник імена → вікова група ===
def task_1():
    users_age_group = {
        "Олег": "Дорослий",
        "Марія": "Підліток",
        "Іван": "Дитина",
        "Світлана": "Дорослий"
    }
    name = input("Введіть ім'я користувача: ")
    age_group = users_age_group.get(name)
    if age_group:
        print(f"{name} належить до вікової групи: {age_group}")
    else:
        print(f"Користувача з ім’ям {name} не знайдено.")


# === Завдання 2: Конвертація числа ===
def task_2():
    try:
        number_input = input("Введіть число: ")
        number = int(number_input)
        print(f"Ціле число: {number}")
    except ValueError:
        print("Помилка: Неможливо конвертувати введення в ціле число.")


# === Завдання 3: Читання файлу ===
def task_3():
    file_path = input("Введіть шлях до файлу: ")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            print("Вміст файлу:")
            print(content)
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")


# === Завдання 4: Імпорт модуля і виклик функції ===
def task_4():
    module_name = input("Введіть назву модуля для імпорту (наприклад, math): ")
    function_name = input("Введіть назву функції (наприклад, sqrt): ")
    try:
        imported_module = __import__(module_name)
        func = getattr(imported_module, function_name)
        print("Результат виклику функції:")
        print(func(16))  # можна змінити параметр
    except ModuleNotFoundError:
        print("Помилка: Модуль не знайдено.")
    except AttributeError:
        print("Помилка: Функція не знайдена у модулі.")
    except Exception as e:
        print(f"Помилка виконання функції: {e}")


# === Головне меню ===
def main():
    while True:
        print("\n=== М
