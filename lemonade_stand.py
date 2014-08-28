#!/usr/bin/env python

__author__ = 'jeremy osborn'

import random
import sys


class LemonadeStand:
    def __init__(self):
        self.day = 0
        self.cash = 100
        self.lemonade = 0
        self.lemonade_price = random.randrange(1, 10)
        self.weather = random.randrange(50, 100)

    def make_lemonade(self):
        while True:
            try:
                lemonade = int(raw_input('How many cups of lemonade will you make (1-10)? '))
                if lemonade in range(1, 11, 1):
                    break
                else:
                    print('Please choose a number between 1 and 10.')
                    continue
            except ValueError, e:
                print ('Please choose a number between 1-10.')
                continue
        self.lemonade += lemonade
        self.cash -= lemonade * (float(self.lemonade_price) / 100)
        self.day += 1
        self.weather = random.randrange(50, 100)
        self.lemonade_price = random.randrange(1, 10)
        print('You made ' + str(lemonade) + ' cups of lemonade!\n')

    def sell_lemonade(self):
        while True:
            try:
                price = int(raw_input('How many cents will you charge for a cup of lemonade? (0-100) '))
                if price in range(0, 101):
                    break
                else:
                    print('Please choose a number between 1 and 100')
                    continue
            except ValueError, e:
                print ('Please choose a number between 1 and 100.')
                continue
        cups = random.randrange(1, 101)  # without heat or price factors, will sell 1-100 cups per day
        price_factor = float(100 - price) / 100  # 10% less demand for each ten cent price increase
        heat_factor = 1 - (((100 - self.weather) * 2) / float(100))  # 20% less demand for each 10 degrees below 100
        if price == 0:
            self.lemonade = 0  # If you set price to zero, all your lemonade sells, for nothing.
            print('All of your lemonade sold for nothing because you set the price to zero.')
            self.day += 1
            self.weather = random.randrange(50, 100)
            self.lemonade_price = random.randrange(1, 10)
        demand = int(round(cups * price_factor * heat_factor))
        if demand > self.lemonade:
            print(
                'You only have ' + str(self.lemonade) + ' cups of lemonade, but there was demand for ' + str(
                    demand) + '.')
            demand = self.lemonade
        revenue = demand * round((float(price) / 100), 2)
        self.lemonade -= demand
        self.cash += revenue
        self.day += 1
        self.weather = random.randrange(50, 100)
        self.lemonade_price = random.randrange(1, 10)
        print('You sold ' + str(demand) + ' cup(s) of lemonade and earned $' + str(revenue) + ' dollars!\n')

    def display_data(self, name):
        if self.day == 0:
            print('\nWelcome ' + name + '!\n')
        print('Day: ' + str(self.day))
        print('Weather: ' + str(self.weather))
        print('Cash: $' + str(self.cash))
        print('Lemonade: ' + str(self.lemonade))
        print('Cost to make Lemonade: $' + str(float(self.lemonade_price) / 100))
        print('============================' + '\n')


def main():
    choice = ''
    while choice not in ['y', 'n']:
        choice = raw_input('Create a new lemonade stand? (y/n) ')
        if choice == 'y':
            name = raw_input('Hi friend. What is your name? ')
            stand = LemonadeStand()
            stand.display_data(name)
            while True:
                choice = raw_input('Enter 1 to make lemonade. Enter 2 to sell lemonade. 3 to quit. ')
                if choice == '1':
                    stand.make_lemonade()
                    stand.display_data(name)
                    continue
                elif choice == '2':
                    stand.sell_lemonade()
                    stand.display_data(name)
                    continue
                elif choice == '3':
                    break
                else:
                    print('You must choose either 1 or 2 or 3.')
                    continue
        elif choice == 'n':
            print('Goodbye!')
            return


main()
