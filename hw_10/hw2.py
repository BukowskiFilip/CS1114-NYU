
from hw10_q1 import Instrument

import random

class Musician:
    def __init__(self, stage_name, instruments):
        self.stage_name = stage_name
        self.instruments = instruments
        self.number_of_instruments = len(self.instruments)

    def __str__(self):
        my_str = f"Musician object '{self.stage_name}, owning a "
        if self.number_of_instruments == 1:
            my_str += f"{(self.instruments[0]).brand} {(self.instruments[0]).model} ({(self.instruments[0]).strength} / 100 strength)"
        elif self.number_of_instruments > 1:
            for i in range(self.number_of_instruments):
                if i == self.number_of_instruments - 1:
                    my_str += "and a"
                my_str += f" {self.instruments[i]}, "
        return my_str

    def pick_instrument(self, instrument_index = None):
        if instrument_index == None:
            return self.instruments[random.randint(0, self.number_of_instruments - 1)]
        else:
            if instrument_index > self.number_of_instruments:
                return self.instruments[-1]
            elif self.instruments == []:
                return None
            elif instrument_index != None:
                for i in range(self.number_of_instruments):
                    if i == instrument_index:
                        return self.instruments[i]
