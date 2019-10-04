# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:38:02 2019

@author: Xandr
"""
import random

class Infond:
    #constructor
    def __init__(self, capital = 560000, all_pai = 100000, hum_pai = 60000, tax = 0.18):
        self.capital = capital
        self.all_pai = all_pai
        self.hum_pai = hum_pai
        self.tax = tax
        self.pai = self.capital / self.all_pai
        self.portfel = {}
        self.profit = 0
    def add_bank(self, name, captl, start, period, percent):
        if 'bank_of_' + name in self.portfel.keys():
            self.portfel['bank_of_' + name].append([captl, start, period, percent])
            self.capital -= captl
        else:
            self.portfel['bank_of_' + name] = []
            self.portfel['bank_of_' + name].append([captl, start, period, percent])
            self.capital -= captl
    def add_bank_metal(self, name, count_bank_metal, price_metal):
        if name in [self.portfel.keys()]:
            self.portfel[name] += count_bank_metal
            self.capital -= (count_bank_metal * price_metal)
        else:
            self.portfel[name] = count_bank_metal
            self.capital -= (count_bank_metal * price_metal)
    def add_actions(self, name, count_actions, price_action):
        if name in self.portfel.keys():
            self.portfel[name] += count_actions
            self.capital -= (count_actions * price_action)
        else:
            self.portfel[name] = count_actions
            self.capital -= (count_actions * price_action)
    def setProfit_bank(self, month):
        for i in self.portfel.keys():
            if i[0:8] == 'bank_of_':
                for j in self.portfel[i]:
                    lst_depoz = []
                    if month == j[1] + j[2]:
                        self.profit = self.profit + round(j[0] * j[3], 2)
                        self.capital += j[0]
                        lst_depoz.append(j)
                    # print(lst_depoz)
                    for k in lst_depoz:
                        self.portfel[i].remove(k)
                print(self.portfel)
                if self.portfel[i] == []:
                    self.portfel.pop(i)
    def sellMetal(self, name, count, price_metal):
        if name in [self.portfel.keys()]:
            if count > self.portfel[name]:
                print("You don\'t have " + str(count) + " units of " + name)
            else:
                self.portfel[name] -= count
                self.profit = self.profit + round(count * price_metal, 2)
    def sellAction(self, name, count, price_action):
        if name in self.portfel.keys():
            if count > self.portfel[name]:
                print("You don\'t have " + str(count) + " actions of " + name)
            else:
                self.portfel[name] -= count
                self.profit = self.profit + round(count * price_action, 2)
    def setCapital(self):
        self.capital += round(self.profit * self.tax, 2)
    def setTax(self):
        return round(self.profit * self.tax, 2)
class Bank:
    def __init__(self):
        name_list = ['Pryvat', 'Aval', 'Oschad', 'UkrEximBank']
        self.bank_name = name_list[random.randint(0, 3)]
        self.bank_period = random.choice([3,6,9,12])
        self.bank_percent = round(0.3 * random.random(), 2)
class BankMetal:
    def __init__(self):
        name_list = ['gold', 'platinum', 'silver']
        self.BankMetal_name = name_list[random.randint(0, 2)]
        if self.BankMetal_name == 'gold':
            self.BankMetal_price = 1536 + round(300 * random.random() * random.choice([-1,0,1]))
        elif self.BankMetal_name == 'platinum':
            self.BankMetal_price = 2346 + round(300 * random.random() * random.choice([-1, 0, 1]))
        else:
            self.BankMetal_price = 21 + round(4 * random.random() * random.choice([-1, 0, 1]))
class Actions:
    def __init__(self):
        name_list = ['metivest', 'ukrtelecom', 'kyivstar']
        self.Actions_name = name_list[random.randint(0, 2)]
        self.Actions_price = 10 + round(3 * random.random() * random.choice([-1,0,1]))               
# fond = Infond()
# fond.add_bank('pb', 10000, 3, 3, 0.12)
# fond.add_bank('pb', 5000, 3, 3, 0.12)
# fond.add_bank_metal('gold', 5, 1536)
# fond.add_bank_metal('plt', 5, 2536)
# fond.add_actions('metivest', 100, 12.5)
# fond.setProfit_bank(6)
# fond.sellMetal('gold', 3, 1245)
# fond.sellMetal('plt', 6, 1245)
# fond.sellAction('metivest', 20, 11.5)
# print(fond.portfel)