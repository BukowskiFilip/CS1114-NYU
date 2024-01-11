import random


class Instrument:
    def __init__(self, model, brand, strength):
        self.model = model
        self.brand = brand
        self.strength = strength

    def __str__(self):
        return f"{self.brand} {self.model} ({self.strength} / 100 strength)"

    def does_break(self):
        random_value = random.random()
        if random_value < (0.5 * self.strength):
            return True
        else:
            return False
