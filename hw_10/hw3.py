
from hw10_q1 import Instrument
from hw10_q2 import Musician
import random

def get_name_of_battle_winner(m1, m2):
    if m1.number_of_instruments == 0 and m2.number_of_instruments > 0:
        return m2.stage_name
    elif m2.number_of_instruments == 0 and m1.number_of_instruments > 0:
        return m1.stage_name
    elif m1.number_of_instruments == 0 and m2.number_of_instruments == 0:
        return "NO CONTEST!"

    else:
        i1 = m1.pick_instrument()
        print("{} picked a {}!".format(m1.stage_name, i1))
        i2 = m2.pick_instrument()
        print("{} picked a {}!".format(m2.stage_name, i2))

        if i1.strength > i2.strength:
            if i1.does_break():
                print("{}'s {} broke!".format(m1.stage_name,i1.model))
                return m2.stage_name
            else:
                return m1.stage_name

        elif i1.strength < i2.strength:
            if i2.does_break():
                print("{}'s {} broke!".format(m2.stage_name, i2.model))
                return m1.stage_name
            else:
                return m2.stage_name
        else:
            print("Both musician's instruments are the same strength. The winner will be decided by the whim of chance.")
            m1_wins = False
            m2_wins = False
            winner = random.choices('HT')

            if winner == 'H':
                m1_wins = True
                return m1.stage_name
            else:
                m2_wins = True
                return m2.stage_name

def main():
    danelectro = Instrument("Stock '59", "Danelectro", 0.25)
    fender_vi = Instrument("VI Bass", "Fender", 0.99)
    four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
    gear = [danelectro, fender_vi, four_double_o_one]

    sad_musician = Musician("Robert Smith", gear)
    less_sad_musician = Musician("Miki Berenyi", gear)

    number_of_duels = 10
    for duel_number in range(number_of_duels):
        winner_name = get_name_of_battle_winner(sad_musician, less_sad_musician)
        print(f"THE WINNER OF DUEL #{duel_number + 1} IS {winner_name}!", end="\n\n")
main()
