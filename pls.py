import tkinter as tk

from fractions import Fraction
import math


window = tk.Tk()
window.title("What Are the Odds?")
# window.overrideredirect(True)
window.geometry("500x500")
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

num_boxes += 1
entry_label = tk.Label(window, text=f"Pick {num_boxes}:", bg="#F6DB79", font=("Helvetica", 11))
entry_label.grid(row=num_boxes + 1, column=0, padx=1, pady=10)
entry_box = tk.Entry(window, width=5, fg="#CB769E", bg="#CBE7F6",
                     justify='center', font=("Helvetica", 11, "bold"))
entry_box.grid(row=num_boxes + 1, column=1, padx=1, pady=10)
entry_boxes.append(entry_box)
decimal_parlay_odds = math.prod(decimal_odds)

parlay_label = tk.Label(window, text="Parlay:", font=("Helvetica", 12))
parlay_label.grid(row=num_boxes + 2, column=0, pady=10)


parlay_label = tk.Label(window, text="Parlay:", font=("Helvetica", 12))
parlay_label.grid(row=num_boxes + 2, column=0, pady=10)


# Bind the key press event to the handle_key_press function

def add_entry_box():
    key_handle_pressed("m")
    global num_boxes
    num_boxes += 1

    # Add entry box



    if num_boxes < 5:
        entry_label = tk.Label(window, text=f"Pick {num_boxes}:", bg="#F6DB79", font=("Helvetica", 11))
        entry_label.grid(row=num_boxes + 1, column=0, padx=1, pady=10)
        entry_box = tk.Entry(window, width=5, fg="#CB769E", bg="#CBE7F6",
                             justify='center', font=("Helvetica", 11, "bold"))
        entry_box.grid(row=num_boxes + 1, column=1, padx=1, pady=10)
        entry_boxes.append(entry_box)
        decimal_parlay_odds = math.prod(decimal_odds)

        parlay_label = tk.Label(window, text="Parlay:", font=("Helvetica", 12))
        parlay_label.grid(row=num_boxes + 2, column=0, pady=10)

    else:
        validate_button.grid_forget()



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
    parlay_odds_label.grid(row=num_boxes + 1, column=1, padx=1, pady=5)
    # TODO: decimal parlay odds
    decimal_parlay_label = tk.Label(window, text=decimal_parlay_odds, fg="green", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
    decimal_parlay_label.grid(row=num_boxes + 1, column=2, padx=1, pady=5)
    # TODO: probability parlay odds
    prob_parlay_label = tk.Label(window, text=prob_parlay_odds, fg="green", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
    prob_parlay_label.grid(row=num_boxes + 1, column=3, padx=1, pady=5)
    # TODO: fraction parlay odds
    frac_parlay_label = tk.Label(window, text=frac_parlay[0], fg="green", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
    frac_parlay_label.grid(row=num_boxes + 1, column=4, padx=1, pady=5)





# window = tk.Tk()
# window.title("What Are the Odds?")
# # window.overrideredirect(True)
# window.geometry("500x500")



window.configure(background='#CBE7F6')
window.columnconfigure(0, weight=1)
number_of_columns = 5



american_label = tk.Label(window, text="American", fg="#CB769E", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
american_label.grid(row=1, column=1, padx=11, pady=3)

# Add a label widget for the decimal odds
decimal_label = tk.Label(window, text="Decimal", fg="#F47E3E", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
decimal_label.grid(row=1, column=2, padx=15, pady=3)

# Add a label widget for the prob odds
prob_label = tk.Label(window, text="Probability", fg="#7E75D1", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
prob_label.grid(row=1, column=3, padx=15, pady=3)

# Add a label widget for the fraction odds
fraction_label = tk.Label(window, text="Fractional", fg="#3B5168", bg="#CBE7F6", font=("Helvetica", 12, "bold"))
fraction_label.grid(row=1, column=4, padx=15, pady=3)




# Add an entry widget for user input
# entry = tk.Entry(window, width=5, font=("Helvetica", 12))
# entry.grid(row=1, column=0, pady=10, sticky="w")

# Add a button widget to add entry boxes
validate_button = tk.Button(window, text="Add Odds", command=add_entry_box, height=1, width=7)
validate_button.grid(row=num_boxes + 7, column=0, padx=5, pady=5)

def key_handle_pressed(event):
    window.bind("m", add_entry_box)

# Add a button widget to retrieve picks
get_picks_button = tk.Button(window, text="Parlay", command=lambda: get_picks())
get_picks_button.grid(row=num_boxes + 9, column=0, padx=5, pady=10, sticky="S")



# Run the event loop
window.mainloop()