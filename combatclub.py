import random
import emoji

# import os
'''with open('test.htm','w',encoding='utf-8-sig') as f:
    f.write('\U0001f44d')
os.startfile('test.htm')'''

hitnow = 'y'
hit = ''
unit = ['Alissa', 'Miu']
try_count = 0


class Warrior:
    def setHealth(self, hp):
        self.health = hp

    def setDamage(self, hit):
        damage = self.health - hit
        self.health = damage
        return damage


# ---------------------------------------------------------------
unit_1 = Warrior()
unit_2 = Warrior()
unit_1.setHealth(100)
unit_2.setHealth(100)
# ---------------------------------------------------------------

while (unit_1.health > 0) and (unit_2.health > 0) and hitnow == 'y':
    r = random.randint(1, 2)
    if r == 1:
        unit_2.setDamage(20)
        print(emoji.emojize('Warrior Alissa got a hit :facepunch:,\n:hospital: Health: ', use_aliases=True),
              unit_2.health, 'hp')
    else:
        unit_1.setDamage(20)
        print(emoji.emojize('Warrior Miu got a hit :facepunch:,\n:hospital: Health: ', use_aliases=True), unit_1.health,
              'hp', end='\n')
    if unit_1.health != 0 and unit_2.health != 0:
        hit = input('Hit now? y/n: ')
        hitnow = hit
        while (hit != 'y') and (hit != 'n') and try_count < 3:
            try_count += 1
            hit = input('make a right choice y or n: ')
            hitnow = hit
            if try_count >= 3:
                print(emoji.emojize(':hourglass_flowing_sand: Your time is out!', use_aliases=True))
                break
        if hit == 'n':
            print(emoji.emojize('The battle was not completed :bomb: :gun:', use_aliases=True))
            break
    # --------------------------------------------------------------

    if unit_1.health == 0:
        print('Game Over! Warrior ', unit[0], emoji.emojize(' is a winner! :trophy:', use_aliases=True))
        print('But ', unit[1], emoji.emojize(' is :heart: anyway', use_aliases=True))
    elif unit_2.health == 0:
        print('Game Over! Warrior ', unit[1], emoji.emojize(' is a winner! :trophy:', use_aliases=True))
        print('But ', unit[0], emoji.emojize(' is :heart: anyway', use_aliases=True))
norr312 = 'no.rr 312'
print(emoji.emojize('\n:registered:Designed by :honeybee: ', use_aliases=True) + norr312.upper() + ' studio with Python 3.7 2019')