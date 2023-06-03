from __future__ import print_function
import math
from equations import Options
from art import logo
import cls
import sys
import os
import time
import colorama
from colorama import Fore

'''
Clear Screen for all OS's - by carmine-falcone!
CLS!
'''
#Vars
system = sys.platform
python_version = sys.version[1]


def cls():
    if 'linux' in system:
        os.system("clear && printf '\e[3J'")
    elif 'windows' in system or 'Windows' in system:
        os.system("cls")
    else:
        n = '\n'*250
        print(n)






plus = '+'
betslip = []
decimal_odds = []
prob_odds = []
american_odds = []
more_picks = True


def as_currency(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)

"""HERE............."""
print(Fore.LIGHTWHITE_EX + logo)
def parlay_calculator():
    more_picks = True
    while more_picks:
        text_color_input = (Fore.RESET + "How many legs are in your parlay?: ")
        try:
            num_events = int(input(text_color_input))
            break
        except ValueError:
            print("Please enter a valid number.")
    for i in range(num_events):
        while True:
            try:
                user_picks = int(input(f"What Are The Odds of Pick {i + 1}?: "))
                if user_picks >= 100:
                    betslip.append(user_picks)

                elif user_picks <= -100:
                    betslip.append(user_picks)

                break
            except ValueError:
                print("Please enter a valid number.")

    for user_picks in betslip:
        if user_picks >= 100:
            decimal_conversion = 1 + (user_picks / 100)
            decimal_odds.append(decimal_conversion)
            prob_percent = (1 / decimal_conversion) * 100
            prob_odds.append(prob_percent)
        elif user_picks <= -100:
            decimal_conversion = (1 - (100 / user_picks))
            decimal_odds.append(decimal_conversion)
            prob_percent = (1 / decimal_conversion) * 100
            prob_odds.append(prob_percent)
        else:
            more_picks = False

    # print("\n" * 80)
    if __name__ == '__main__':
        print("Cleaning Screen!")
        time.sleep(0.5)
        cls()
    print("\b"*50)
    print(logo)
    print(f"Final Betslip: {betslip}")

    # print(decimal_odds)
    dec_parlay_odds = math.prod(decimal_odds)
    # print(dec_parlay_odds)
    usa_parlay_odds = round((dec_parlay_odds - 1) * 100, 1)
    # print(usa_parlay_odds)

    print(f"Your {num_events} Leg Parlay Odds are: {plus}{usa_parlay_odds}")
    print("\n")
    wager_or_more = input("Would you Like to Wager or See More Options?\n"
                          "Type '1' to Wager\nType '2' for More Options: ").lower()
    print("\n")
    if wager_or_more == "1":
        print(f"Odds: {plus}{usa_parlay_odds}")
        wager = int(input("How Much Would you Like to Wager?: $"))
        wager_as_money = as_currency(wager)
        to_win = usa_parlay_odds * (wager / 100)
        to_win_as_money = as_currency(to_win)
        payout = to_win + wager
        payout_as_money = as_currency(payout)
        print(f"Wager: {wager_as_money}\nTo Win: {to_win_as_money}")
        print(f"Potential Payout: {payout_as_money}")
        print("\n")

    elif wager_or_more == "2":
        Options(decimal_odds, betslip, plus, num_events)

parlay_calculator()
white_text_input = (Fore.LIGHTWHITE_EX + 'Want to Make a Parlay? (y/n): ')
while input(white_text_input).lower().strip() == 'y':
    print("\n")
    betslip.clear()
    decimal_odds.clear()
    prob_odds.clear()
    american_odds.clear()
    parlay_calculator()












