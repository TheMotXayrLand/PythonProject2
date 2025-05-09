import random

# --- Класс Pet (Питомец) ---
class Pet:
    def __init__(self, name="Pet"):
        self.name = name
        self.hunger = 0
        self.happiness = 100
        self.alive = True

    def feed(self):
        print(f"{self.name} is being fed.")
        self.hunger = max(0, self.hunger - 10)
        self.happiness = min(100, self.happiness + 5)

    def play(self):
        print(f"{self.name} is playing.")
        self.happiness += 10
        self.hunger += 5

    def day_passes(self):
        self.hunger += 5
        self.happiness -= 5
        if self.hunger > 100 or self.happiness < 0:
            print(f"{self.name} has passed away...")
            self.alive = False

# --- Класс Job ---
job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}

class Job:
    def __init__(self):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

# --- Класс Auto ---
brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}

class Auto:
    def __init__(self):
        self.brand = random.choice(list(brands_of_car))
        data = brands_of_car[self.brand]
        self.fuel = data["fuel"]
        self.strength = data["strength"]
        self.consumption = data["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move.")
            return False

# --- Класс House ---
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

# --- Класс Human ---
class Human:
    def __init__(self, name="Human"):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = None
        self.car = None
        self.home = None

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto()

    def get_job(self):
        if self.car and not self.car.drive():
            self.to_repair()
            return
        self.job = Job()

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        self.satiety = min(100, self.satiety + 5)
        self.home.food = max(0, self.home.food - 5)

    def work(self):
        if not self.car.drive():
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if not self.car.drive():
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            self.money -= 15
            self.gladness += 10
            self.satiety += 2

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            return False
        return True

# --- Класс Student (наследуется от Human) ---
class Student(Human):
    def __init__(self, name="Student"):
        super().__init__(name)
        self.pet = Pet(name=f"{self.name}'s Pet")

    def play_with_pet(self):
        if self.pet and self.pet.alive:
            print(f"{self.name} is playing with {self.pet.name}")
            self.pet.play()
            self.gladness += 1

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            self.get_home()
            print("Settled in the house")
        if self.car is None:
            self.get_car()
            print(f"Bought a car: {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"Got a job: {self.job.job} with salary {self.job.salary}")

        print(f"\n{' Day ' + str(day) + ' of ' + self.name + "'s life ":=^50}")
        print(f"Money: {self.money} | Satiety: {self.satiety} | Gladness: {self.gladness}")
        print(f"Food: {self.home.food} | Mess: {self.home.mess}")
        print(f"Car: {self.car.brand} | Fuel: {self.car.fuel} | Strength: {self.car.strength}")

        # Жизнь питомца
        if self.pet:
            self.pet.day_passes()
            if not self.pet.alive:
                print(f"{self.name} is grieving the loss of {self.pet.name}")
                self.gladness -= 15
                self.pet = None
            else:
                if self.pet.happiness > 60:
                    self.gladness += 2
                elif self.pet.happiness < 30:
                    self.gladness -= 2

                pet_action = random.randint(1, 4)
                if pet_action == 1:
                    self.play_with_pet()
                elif pet_action == 2:
                    print(f"{self.name} feeds {self.pet.name}")
                    self.pet.feed()

        dice = random.randint(1, 4)
        if self.satiety < 20:
            print(f"{self.name} decides to eat.")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("Too messy to chill! Cleaning instead.")
                self.clean_home()
            else:
                print("Chilling to recover gladness.")
                self.chill()
        elif self.money < 0:
            print("Working to earn money.")
            self.work()
        elif self.car.strength < 15:
            print("Repairing car.")
            self.to_repair()
        elif dice == 1:
            self.chill()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.clean_home()
        elif dice == 4:
            self.shopping("delicacies")
        return True

# --- Симуляция жизни студента ---
nick = Student(name="Nick")
for day in range(1, 366):
    if not nick.live(day):
        break
