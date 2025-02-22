class Animal:
    def __init__(self, name, eating_habit, sleep_pattern, movement, aggression, water_activity):
        self.name = name
        self.eating_habit = eating_habit
        self.sleep_pattern = sleep_pattern
        self.movement = movement
        self.aggression = aggression
        self.__water_activity = water_activity  # Private attribute

    def make_sound(self):
        print(f"{self.name} makes a unique sound.")

    def eat(self):
        print(f"{self.name} is enjoying its {self.eating_habit} meal.")

    def sleep(self):
        print(f"{self.name} sleeps {self.sleep_pattern}.")

    def move(self):
        print(f"{self.name} moves by {self.movement}.")

    def attack(self):
        print(f"{self.name} shows aggression by {self.aggression}.")

    def swim(self):
        print(f"{self.name} is engaging in {self.__water_activity}.")