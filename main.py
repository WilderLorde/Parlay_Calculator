from fractions import Fraction
import math


plus = '+'
betslip = []
decimal_odds = []
probabilities = []
probabilities_with_percent = []
fraction_odds = []
more_picks = True

while more_picks:
	pick = int(input("Enter Odds or Type '0' to Parlay Current Odds: "))
	if pick > 0 or pick < 0:
		betslip.append(pick)
	if pick == 0:
		more_picks = False
# TODO: Decimal Odds
	if pick > 0:
		decimal_conversion = round(1 + (pick / 100), 2)
		decimal_odds.append(decimal_conversion)
	elif pick < 0:
		decimal_conversion = round(1 - (100 / pick), 2)
		decimal_odds.append(decimal_conversion)
# TODO: Probability Odds
	if pick > 0:
		prob_conversion = round((100 / (pick + 100)) * 100, 1)
		prob_percent = str(prob_conversion) + '%'
		probabilities_with_percent.append(prob_percent)
		probabilities.append(prob_conversion)
	elif pick < 0:
		prob_conversion = round((pick / (pick + 100)) * 100, 1)
		prob_percent = str(prob_conversion) + '%'
		probabilities_with_percent.append(prob_percent)
		probabilities.append(prob_conversion)
# TODO: Fractions Odds
	if pick > 0:
		fraction_conversion = str(Fraction(pick / 100).limit_denominator(100))
		fraction_odds.append(fraction_conversion)
	elif pick < 0:
		fraction_conversion = str(Fraction(pick / 100).limit_denominator(100))
		print(fraction_conversion)
		fraction_odds.append(fraction_conversion)

print("\n")

print(f"Betslip: {betslip}")
print(f"Decimal: {decimal_odds}")
print(f"Probability: {probabilities_with_percent}")
print(f"Fractional: {fraction_odds}")

"""(P(A) + P(B) + P(C)) - (P(A) * P(B)) - (P(A) * P(C)) - (P(B) * P(C)) + (P(A) * P(B) * P(C)"""
if len(decimal_odds) == 3:
	outcome_a = decimal_odds[0]
	print(f"A: {outcome_a}")
	outcome_b = decimal_odds[1]
	print(f"B: {outcome_b}")
	outcome_c = decimal_odds[2]
	print(f"C: {outcome_c}")
	sum_of_probs = 0
	sum_of_probs += (outcome_a + outcome_b + outcome_c)
	print(f"Sum of Probs: {sum_of_probs}")

	product_of_dec = 0
	product_of_dec += (outcome_a * outcome_b * outcome_c)
	"""this is parlay with all events"""
	print(f"Product of dec: {product_of_dec}")
	parlay_percent = ((1 / product_of_dec) * 100)
	print(f"Parlay Percent {parlay_percent}%")
	num_picks = len(betslip)
	american_odds = round((100 / (parlay_percent / 100)) - 100, 2)
	# print(f"Your {num_picks} Leg Parlay Odds are: {plus}{american_odds}")

	a_b = (outcome_a * outcome_b)
	print(f"Outcome Events A and B: {a_b}")
	a_c = (outcome_a * outcome_c)
	print(f"Outcome Events A and B: {a_c}")
	b_c = (outcome_b * outcome_c)
	print(f"Outcome Events B and C: {b_c}")
	all_occur = round((a_b - a_c - b_c), 2)
	print(f"All: {all_occur}")
	at_least_one = (sum_of_probs - all_occur + product_of_dec)
	print(f"At Least 1: {at_least_one}")
	print("\n")
	print(f"Your {num_picks} Leg Parlay Odds are: {plus}{american_odds}")
"""(P(A) + P(B) + P(C) + P(D)) - (P(A) * P(B)) - (P(A) * P(C)) - (P(A) * P(D)) - (P(B) * P(C)) - (P(B) * P(D)) + (P(A) * P(B) * P(C) * P(D)"""
if len(decimal_odds) == 4:
	outcome_a = decimal_odds[0]
	print(f"A: {outcome_a}")
	outcome_b = decimal_odds[1]
	print(f"B: {outcome_b}")
	outcome_c = decimal_odds[2]
	print(f"C: {outcome_c}")
	outcome_d = decimal_odds[3]
	print(f"D: {outcome_d}")
	sum_of_probs = 0
	sum_of_probs += (outcome_a + outcome_b + outcome_c + outcome_d)
	print(f"Sum of Probs: {sum_of_probs}")

	product_of_dec = 0
	product_of_dec += (outcome_a * outcome_b * outcome_c * outcome_d)
	"""this is parlay with all events"""
	print(f"Product of dec: {product_of_dec}")
	parlay_percent = ((1 / product_of_dec) * 100)
	print(f"Parlay Percent {parlay_percent}%")
	num_picks = len(betslip)
	american_odds = round((100 / (parlay_percent / 100)) - 100, 2)
	# print(f"Your {num_picks} Leg Parlay Odds are: {plus}{american_odds}")

	a_b = (outcome_a * outcome_b)
	print(f"Outcome Events A and B: {a_b}")
	a_c = (outcome_a * outcome_c)
	print(f"Outcome Events A and B: {a_c}")
	b_c = (outcome_b * outcome_c)
	print(f"Outcome Events B and C: {b_c}")
	all_occur = round((a_b - a_c - b_c), 2)
	print(f"All: {all_occur}")
	at_least_one = (sum_of_probs - all_occur + product_of_dec)
	print(f"At Least 1: {at_least_one}")
	print("\n")
	print(f"Your {num_picks} Leg Parlay Odds are: {plus}{american_odds}")

num_picks = len(betslip)


# 	if pick > 0:
# 		odds = f"{plus}{pick}"
# 		betslip.append(odds)
# 		decimal_conversion = round(1 + (pick / 100), 2)
# 		decimal_odds.append(decimal_conversion)
# 	elif pick < 0:
# 		betslip.append(pick)
# 		decimal_conversion = round(1 - (100 / pick), 2)
# 		decimal_odds.append(decimal_conversion)
# 	else:
# 		more_picks = False
# print("\n")
#
# num_picks = len(betslip)
# betslip_decimals = math.prod(decimal_odds)
# print(decimal_odds)
# print(sum(decimal_odds))
# print(round(betslip_decimals, 3))
#
# if betslip_decimals > 1.99:
# 	american_odds = round((betslip_decimals - 1) * 100, 2)
# 	parlay = american_odds
# else:
# 	american_odds = round(-100 / (betslip_decimals - 1), 2)
# 	parlay = american_odds
#
# parlay_odds = parlay
#
#
# print(f"Your {num_picks} Leg Parlay Odds are: {plus}{parlay_odds}")
#
# # TODO: get wager amount
# wager = int(input("How Much Will You Wager?: $"))
# calculate = round((wager * betslip_decimals) - wager ,2)
#
# print(f"Your Payout Would Be: ${calculate}")


# TODO: do you want to create another parlay?
