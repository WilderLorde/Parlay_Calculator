import math
from equations import Options


plus = '+'
betslip = []
decimal_odds = []
prob_odds = []
american_odds = []
more_picks = True

while more_picks:
	try:
		num_events = int(input("How many legs are in your parlay?: "))
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
		print(f"\nCurrent Betslip: {betslip}")
	else:
		more_picks = False
print(f"Final Betslip: {betslip}")

# print(decimal_odds)
dec_parlay_odds = math.prod(decimal_odds)
# print(dec_parlay_odds)
usa_parlay_odds = round((dec_parlay_odds - 1) * 100, 1)
# print(usa_parlay_odds)
print(f"Your {num_events} Leg Parlay Odds are: {plus}{usa_parlay_odds}")
print("\n")
wager_or_more = input("Would you Like to Wager or See More Options?\nType 'w' to Wager or 'm' for More Options: ")
print("\n")
if wager_or_more == "w":
	wager = int(input("How Much Would you Like to Wager?: $"))
	to_win = usa_parlay_odds * (wager / 100)
	payout = to_win + wager
	print(f"Wager: ${wager} Odds: {plus}{usa_parlay_odds} To Win: ${to_win}")
	print(f"Potential Payout: ${payout}")
else:
	Options(decimal_odds, betslip, plus, num_events)











