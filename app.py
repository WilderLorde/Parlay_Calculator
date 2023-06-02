# import tkinter as tk
#
# betslip = []
# num_legs = []
# num_boxes = 0  # Variable to store the number of boxes
# window = tk.Tk()
#
# def retrieve_input():
# 	input_value = entry_box.get()
# 	betslip.append(input_value)
# 	print(betslip)
#
# # global num_boxes
# num_boxes += 1
#
# 	# Add entry box
# if num_boxes < 5:
# 	entry_label = tk.Label(window, text=f"Pick {num_boxes}:")
# 	entry_label.grid(row=num_boxes + 1, column=0, padx=1, pady=5)
# 	entry_box = tk.Entry(window, width=5)
# 	entry_box.grid(row=num_boxes + 1, column=1, padx=1, pady=5)
#
# else:
# 	max_label = tk.Label(window, text="You've reached max number of Legs.", font=("Helvetica", 10))
# 	max_label.grid(row=num_boxes + 1, column=2, columnspan=2, padx=1, pady=5)
# 	options_label = tk.Label(window, text="Do you want to Wager?", font=("Helvetica", 10))
# 	options_label.grid(row=num_boxes + 2, column=2, columnspan=2, padx=1, pady=3)
# 	parlay_button = tk.Button(window, text="Parlay", command=lambda: retrieve_input())
# 	parlay_button.grid(row=6, column=0, columnspan=1, padx=1, pady=10)
#
#
# def add_entry_box():
# 	global num_boxes
# 	num_boxes += 1
#
# 	# Add entry box
# 	if num_boxes < 5:
# 		entry_label = tk.Label(window, text=f"Pick {num_boxes}:")
# 		entry_label.grid(row=num_boxes + 1, column=0, padx=1, pady=5)
# 		entry_box = tk.Entry(window, width=5)
# 		entry_box.grid(row=num_boxes + 1, column=1, padx=1, pady=5)
# 		num_legs.append(entry_box)
# 		retrieve_input()
#
# 	else:
# 		max_label = tk.Label(window, text="You've reached max number of Legs.", font=("Helvetica", 10))
# 		max_label.grid(row=num_boxes + 1, column=2, columnspan=2, padx=1, pady=5)
# 		options_label = tk.Label(window, text="Do you want to Wager?", font=("Helvetica", 10))
# 		options_label.grid(row=num_boxes + 2, column=2, columnspan=2, padx=1, pady=3)
# #
# #
# #
# #
# #
# # Create the main window
#
# window.title("What Are the Odds?")
# window.geometry("450x350")
#
# # Add a label widget for the title
# title_label = tk.Label(window, text="What Are the Odds?", font=("Helvetica", 16, "bold"))
# title_label.grid(row=0, column=2, padx=1, pady=10)
#
# # # Add an entry widget for user input
# # entry = tk.Entry(window, width=5, font=("Helvetica", 12))
# # entry.grid(row=2, column=1, padx=1, pady=10)
#
# # Add a button widget for input validation
# validate_button = tk.Button(window, text="Add Picks", command=add_entry_box)
# validate_button.grid(row=1, column=0, columnspan=1, padx=1, pady=10)
#
#
# # Run the event loop
# #
# window.mainloop()
import ctypes
import tkinter as tk
import os
from fractions import Fraction
import math

# Example decimal number


# Convert the decimal number to a fraction with a maximum denominator of 100


# Display the fraction
percent = '%'
plus = '+'
num_boxes = 0
entry_boxes = []  # List to store the entry box objects
picks = []  # List to store the entered values
decimal_odds = []
prob_odds = []
fraction_odds = []

american_odds = []
dec_parlay = []
prob_parlay = []
frac_parlay = []

wagers = []



def add_entry_box():
    global num_boxes
    num_boxes += 1

    # Add entry box
    # if num_boxes < 5:
    #     entry_label = tk.Label(window, text=f"Pick {num_boxes}:", bg="#F6DB79", font=("Helvetica", 11))
    #     entry_label.grid(row=num_boxes + 1, column=0, padx=1, pady=10)
    #     entry_box = tk.Entry(window, width=5, fg="#CB769E", bg="#CBE7F6",
    #                          justify='center', font=("Helvetica", 11, "bold"))
    #     entry_box.grid(row=num_boxes + 1, column=1, padx=1,pady=10)
    #     entry_boxes.append(entry_box)
    #     decimal_parlay_odds = math.prod(decimal_odds)
    #
    #     parlay_label = tk.Button(window, text='Parlay', bg='pale green', width=5, height=1, font=("Helvetica", 12))
    #     parlay_label.grid(row=8, column=0, pady=10)
    #
    #
    #
    # else:
    #     validate_button.grid_forget()
        # parlay_label = tk.Label(window, text="Parlay:", font=("Helvetica", 10))
        # parlay_label.grid(row=num_boxes + 2, column=0, padx=1, pady=5)
        # options_label = tk.Label(window, text="Do you want to Wager?", font=("Helvetica", 10))
        # options_label.grid(row=num_boxes + 3, column=2, columnspan=2, padx=1, pady=3)

    # Add entry box to the list



def get_picks():
    global picks
    picks = []  # Clear the list before retrieving the values


    # Retrieve values from the entry boxes
    for entry_box in entry_boxes:
        value = entry_box.get()
        odds = int(value)
        picks.append(odds)

    print(picks)  # Print the list of picks
    for odds in picks:
        if odds >= 100:
            # TODO: decimal[0]
            decimal_conversion = round(1 + (odds / 100), 2)
            decimal_odds.append(decimal_conversion)
            decimal_odds0 = tk.Label(window, text=decimal_odds[0],
                                     fg="#F47E3E", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
            decimal_odds0.grid(row=2, column=2, padx=2, pady=5)
            # TODO: prob[0]
            prob_percent = round((1 / decimal_conversion) * 100, 1), percent
            prob_odds.append(prob_percent)
            prob_odds0 = tk.Label(window, text=prob_odds[0], fg="#7E75D1", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
            prob_odds0.grid(row=2, column=3, padx=2, pady=5)
            # TODO: fract[0]
            fraction = str(Fraction(odds / 100).limit_denominator(100))
            fraction_odds.append(fraction)
            frac_odds0 = tk.Label(window, text=fraction_odds[0], fg="#3B5168", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
            frac_odds0.grid(row=2, column=4, padx=2, pady=5)
    for odds in picks:
        if odds >= 100:
            #TODO: decimal[1]
            decimal_odds1 = tk.Label(window, text=decimal_odds[1],
                                     fg="#F47E3E", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
            decimal_odds1.grid(row=3, column=2, padx=1, pady=5)
            # TODO: prob[1]
            prob_odds1 = tk.Label(window, text=prob_odds[1], fg="#7E75D1", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
            prob_odds1.grid(row=3, column=3, padx=1, pady=5)
            # TODO: fract[1]
            frac_odds1 = tk.Label(window, text=fraction_odds[1], fg="#3B5168", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
            frac_odds1.grid(row=3, column=4, padx=1, pady=5)
            #TODO: parlay odds
    for odds in picks:
        if odds >= 100:
            # TODO: decimal[2]
            decimal_odds2 = tk.Label(window, text=decimal_odds[2],
                                     fg="#F47E3E", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
            decimal_odds2.grid(row=4, column=2, padx=1, pady=5)
            # TODO: prob[2]
            prob_odds2 = tk.Label(window, text=prob_odds[2], fg="#7E75D1", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
            prob_odds2.grid(row=4, column=3, padx=1, pady=5)
            # TODO: fract[2]
            frac_odds2 = tk.Label(window, text=fraction_odds[2],
                                  fg="#3B5168", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
            frac_odds2.grid(row=4, column=4, padx=1, pady=5)
    for odds in picks:
        if odds >= 100:
            # TODO: decimal[3]
            decimal_odds3 = tk.Label(window, text=decimal_odds[3],
                                     fg="#F47E3E", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
            decimal_odds3.grid(row=5, column=2, padx=1, pady=5)
            # TODO: prob[3]
            prob_odds3 = tk.Label(window, text=prob_odds[3], fg="#7E75D1", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
            prob_odds3.grid(row=5, column=3, padx=1, pady=5)
            # TODO: fract[3]
            frac_odds3 = tk.Label(window, text=fraction_odds[3],
                                  fg="#3B5168", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
            frac_odds3.grid(row=5, column=4, padx=1, pady=5)

        elif odds <= -100:
            decimal_conversion = round(1 - (100 / odds), 2)
            decimal_odds.append(decimal_conversion)

            decimal_odds1 = tk.Label(window, text=decimal_odds[0], font=("Helvetica", 12))
            decimal_odds1.grid(row=2, column=2, padx=1, pady=5)

            prob_percent = round((1 / decimal_conversion) * 100, 1), percent
            prob_odds.append(prob_percent)

            prob_odds1 = tk.Label(window, text=prob_odds[0], fg="#7E75D1", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
            prob_odds1.grid(row=2, column=3, padx=1, pady=5)

            fraction = str(Fraction(-100 / odds).limit_denominator(100))
            fraction_odds.append(fraction)

            frac_odds1 = tk.Label(window, text=fraction_odds[0], font=("Helvetica", 12))
            frac_odds1.grid(row=2, column=4, padx=1, pady=5)
            # Add a label widget for the american parlay odds
    print(f"Final Betslip: {picks}")
    print(f"Decimal odds: {decimal_odds}")
    print(f"prob odds: {prob_odds}")
    print(f"Fractional Odds: {fraction_odds}")

    decimal_parlay_odds = round(math.prod(decimal_odds), 1)
    dec_parlay.append(decimal_parlay_odds)

    prob_parlay_odds = round((1 / decimal_parlay_odds) * 100, 1), percent
    prob_parlay.append(prob_parlay_odds)

    american_parlay_odds = plus, round((decimal_parlay_odds - 1) * 100, 1)
    for_frac = round((decimal_parlay_odds - 1) * 100, 1)
    american_odds.append(american_parlay_odds)

    fraction_parlay_odds = str(Fraction(for_frac / 100).limit_denominator(100))
    frac_parlay.append(fraction_parlay_odds)
    print(f"parlay odds: {plus}{american_parlay_odds}")

    #TODO: american parlay odds
    parlay_odds_label = tk.Label(window, text=american_odds[0], fg="green", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
    parlay_odds_label.grid(row=6, column=1, padx=1, pady=5)
    # TODO: decimal parlay odds
    decimal_parlay_label = tk.Label(window, text=decimal_parlay_odds, fg="green", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
    decimal_parlay_label.grid(row=6, column=2, padx=1, pady=5)
    # TODO: probability parlay odds
    prob_parlay_label = tk.Label(window, text=prob_parlay_odds, fg="green", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
    prob_parlay_label.grid(row=6, column=3, padx=1, pady=5)
    # TODO: fraction parlay odds
    frac_parlay_label = tk.Label(window, text=frac_parlay[0], fg="green", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
    frac_parlay_label.grid(row=6, column=4, padx=1, pady=5)

    some_list = ['Parlay', 'At Least 1', 'At Least 2', 'Round Robin']

    buttons = []  # create global variable
    for item in some_list:
        b = tk.Button(window, text=item, width=10)
        buttons.append(b)

    wager_label.grid(row=6, column=0, padx=1, pady=10)




def toggle_text():

    if wager_label['text'] == 'Wager':
        wager_label['text']  = 'Hide'

        for i, b in enumerate(buttons, 6):
            b.grid(row=i + 7, column=0, padx=10)

    else:
        wager_label['text'] = 'Wager'

        for b in buttons:
            b.grid_forget()

def bet_offers():

    offers_label = tk.Label(window, text="Choose a Bet Option", fg="hot pink", bg="#CBE7F6", font=("Helvetica", 15, "bold"))
    offers_label.grid(column=1, row=9, columnspan=4)


    # normal_parlay_btn = tk.Button(window, text="Parlay", width=10)
    buttons.append(normal_parlay_btn)
    normal_parlay_btn.grid(column=1, row=10, padx=5)

    at_least_1_btn = tk.Button(window, text='At Least 1', width=10)
    buttons.append(at_least_1_btn)
    at_least_1_btn.grid(column=2, row=10, padx=5)

    at_least_2_btn = tk.Button(window, text='At Least 2', width=10)
    buttons.append(at_least_2_btn)
    at_least_2_btn.grid(column=3, row=10, padx=5)

    round_robin_btn = tk.Button(window, text='Round Robin', width=10)
    buttons.append(round_robin_btn)
    round_robin_btn.grid(column=4, row=10, padx=5)

def wager():
    details_label = tk.Label(window, text="Wager Amount: $", fg="green", bg="#CBE7F6", font=("Helvetica", 11, "bold"))
    details_label.grid(row=11, column=2, pady=10, padx=1)


    wager_box = tk.Entry(window, width=5, bg="white",
                         justify='center', font=("Helvetica", 11, "bold"))
    wager_box.grid(row=11, column=3, padx=1)
    wager_amount = wager_box.get()
    payout = american_odds * (wager_amount / 100)
    wager_total.append(wager_amount)
    bet_btn.grid(row=12, column=2)

def bet_details():
    to_win = american_odds * (wager_total[0] / 100)
    payout_label = tk.Label(window, text=f"Total payout: ${to_win}", fg="green", bg="#CBE7F6",
                            font=("Helvetica", 11, "bold"))
    payout_label.grid(row=13, column=2)




# def restart():
#     window.destroy()
#     parlay_main()




window = tk.Tk()
window.title("Parlay Calculator")
# window.overrideredirect(True)
window.geometry("500x500")
# title_bar = tk.Frame(window, bg="#ADBCA5", relief='groove', bd=2, highlightthickness=0)
#
# close_button = tk.Button(title_bar, anchor="nw", text='X', command=window.destroy, bg="white",
#                          padx=1, pady=1, activebackground="red", bd=0, font="bold", fg="red", highlightthickness=0)
# title_bar.grid(columnspan=6)
# close_button.grid(column=0, row=0, sticky="w")


window.configure(background='#CBE7F6')
window.columnconfigure(0, weight=1)
number_of_columns = 5


# Add a label widget for the title
title_label = tk.Label(window, text="What Are the Odds?",fg="hot pink", bg="#CBE7F6", font=("Helvetica", 18, "bold"))
title_label.grid(row=0, column=1, columnspan=4, pady=10)

american_label = tk.Label(window, text="American", fg="#CB769E", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
american_label.grid(row=1, column=1, padx=10, pady=3)

# Add a label widget for the decimal odds
decimal_label = tk.Label(window, text="Decimal", fg="#F47E3E", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
decimal_label.grid(row=1, column=2, padx=10, pady=3)

# Add a label widget for the prob odds
prob_label = tk.Label(window, text="Probability", fg="#7E75D1", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
prob_label.grid(row=1, column=3, padx=10, pady=3)

# Add a label widget for the fraction odds
fraction_label = tk.Label(window, text="Fractional", fg="#3B5168", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
fraction_label.grid(row=1, column=4, padx=10, pady=3)




pick1 = tk.Label(window, text=f"Pick 1:", bg="#F6DB79", font=("Helvetica", 11))
pick1.grid(row=2, column=0, padx=10, pady=10)
pick1_box = tk.Entry(window, width=5, fg="#CB769E", bg="white",
                     justify='center', font=("Helvetica", 11, "bold"))
pick1_box.grid(row=2, column=1, padx=1, pady=10)
pick1_box.focus()
entry_boxes.append(pick1_box)

pick2 = tk.Label(window, text=f"Pick 2:", bg="#F6DB79", font=("Helvetica", 11))
pick2.grid(row=3, column=0, padx=10, pady=10)
pick2_box = tk.Entry(window, width=5, fg="#CB769E", bg="white",
                     justify='center', font=("Helvetica", 11, "bold"))
pick2_box.grid(row=3, column=1, padx=1, pady=10)
entry_boxes.append(pick2_box)

pick3 = tk.Label(window, text=f"Pick 3:", bg="#F6DB79", font=("Helvetica", 11))
pick3.grid(row=4, column=0, padx=10, pady=10)
pick3_box = tk.Entry(window, width=5, fg="#CB769E", bg="white",
                     justify='center', font=("Helvetica", 11, "bold"))
pick3_box.grid(row=4, column=1, padx=1, pady=10)
entry_boxes.append(pick3_box)

pick4 = tk.Label(window, text=f"Pick 4:", bg="#F6DB79", font=("Helvetica", 11))
pick4.grid(row=5, column=0, padx=10, pady=10)
pick4_box = tk.Entry(window, width=5, fg="#CB769E", bg="white",
                     justify='center', font=("Helvetica", 11, "bold"))
pick4_box.grid(row=5, column=1, padx=10, pady=10)
entry_boxes.append(pick4_box)
# decimal_parlay_odds = math.prod(decimal_odds)

all_odds = tk.Label(window, text=f"Parlay:", fg="hot pink", bg="#CBE7F6", font=("Helvetica", 11, "bold"))
all_odds.grid(row=6, column=0, padx=1, pady=10)

wager_total = []




parlay_label = tk.Button(window, text='Parlay', bg='pale green', width=5, height=1,
                         font=("Helvetica", 12), command=lambda: get_picks())
parlay_label.grid(row=6, column=0, pady=10)



# clear_label = tk.Button(window, text='Clear', bg='indian red', width=5, height=1,
#                          font=("Helvetica", 12), command=lambda: restart())
# print("clear clicked")
# clear_label.grid(row=10, column=0, pady=10)

some_list = ['Parlay', 'At Least 1', 'At Least 2', 'Round Robin']

buttons = []  # create global variable
normal_parlay_btn = tk.Button(window, text="Parlay", width=10)
buttons.append(normal_parlay_btn)

at_least_1_btn = tk.Button(window, text='At Least 1', width=10)
buttons.append(at_least_1_btn)

at_least_2_btn = tk.Button(window, text='At Least 2', width=10)
buttons.append(at_least_2_btn)

round_robin_btn = tk.Button(window, text='Round Robin', width=10)
buttons.append(round_robin_btn)

print(buttons)

normal_parlay_btn = tk.Button(window, text="Parlay", width=10, command=lambda: wager())

wager_label = tk.Button(window, text='Wager', bg='green', width=5, height=1,
                        font=("Helvetica", 12, "bold"), command=lambda: bet_offers())
print("wager clicked")
# wager_label.grid(row=6, column=0, padx=1, pady=10)
bet_btn = tk.Button(window, text="Bet", bg='green', width=5, height=1,
                    font=("Helvetica", 12, "bold"), command=lambda: bet_details())
window.mainloop()


#TODO: wager






