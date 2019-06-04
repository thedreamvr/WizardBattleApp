from actors import Wizard, Creature, SmallAnimal, Dragon

import random
import time

def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------------')
    print('           WIZARD GAME APP')
    print('--------------------------------')
    print()


def game_loop():
    
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 20, 30, True),
        Wizard('Evil Wizard', 50)
    ]

    hero = Wizard('Gandolf', 40)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appear from a dark and foggy forest...'.format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard run and hides taking time to recover...")
                time.sleep(5)
                print("The hero has returned revived.")
        elif cmd == 'r':
            print("The wizard has become unsure of his power and flees!!!")
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'.format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print("Ok, exiting game..., bye!")
            break

        if not creatures:
            print("You have defeated all the creatures and saved the kingdom from the Evil Wizard!")


if __name__ == '__main__':
    main()

