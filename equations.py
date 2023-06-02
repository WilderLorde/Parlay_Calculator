
class Options:

	def __init__(self, decimal_odds, betslip, plus, num_events):

		options = input("Choose a Option: (At Least 1/At Least 2): ")
		if options == "At Least 1":
			# # # print(f"Decimal Odds: {decimal_odds}")
			if num_events == 3:
				outcome_a = decimal_odds[0]
				outcome_b = decimal_odds[1]
				outcome_c = decimal_odds[2]
				percent_a = round((1 / outcome_a), 2)
				percent_b = round((1 / outcome_b), 2)
				percent_c = round((1 / outcome_c), 2)
				add_abc = percent_a + percent_b + percent_c
				multiply_ab = (percent_a * percent_b)
				# print(multiply_ab)
				multiply_ac = (percent_a * percent_c)
				multiply_bc = (percent_b * percent_c)
				# print(multiply_bc)
				product_all = (percent_a * percent_b * percent_c)
				at_least = add_abc - multiply_ab - multiply_ac - multiply_bc + product_all
				at_least_percent = round((at_least * 100), 1)
				# print(at_least_percent)
				at_least_decimal = 1 / (at_least_percent / 100)
				# print(at_least_decimal)
			elif num_events == 4:
				outcome_a = decimal_odds[0]
				outcome_b = decimal_odds[1]
				outcome_c = decimal_odds[2]
				outcome_d = decimal_odds[3]
				percent_a = round((1 / outcome_a), 2)
				percent_b = round((1 / outcome_b), 2)
				percent_c = round((1 / outcome_c), 2)
				percent_d = round((1 / outcome_d), 2)
				# print(percent_a, percent_b, percent_c)
				add_abcd = percent_a + percent_b + percent_c + percent_d
				# print(add_abcd)
				multiply_ab = (percent_a * percent_b)
				# print(multiply_ab)
				multiply_ac = (percent_a * percent_c)
				# print(multiply_ac)
				multiply_ad = (percent_a * percent_d)
				# print(multiply_ac)
				multiply_bc = (percent_b * percent_c)
				# print(multiply_bc)
				multiply_bd = (percent_b * percent_d)
				# print(multiply_bd)
				multiply_cd = (percent_c * percent_d)
				# print(multiply_cd)
				product_all = (percent_a * percent_b * percent_c * percent_d)
				# print(product_all)
				# print(f"{add_abcd} - {multiply_ab} - {multiply_ac} - {multiply_ad} - {multiply_bc} - {multiply_bd} - {multiply_cd} "
				#       f"+ {product_all}")
				at_least = add_abcd - multiply_ab - multiply_ac - multiply_ad - multiply_bc - multiply_bd - multiply_cd + product_all
				at_least_percent = round((at_least * 100), 1)
				# print(at_least_percent)
			at_least_decimal = 1 / (at_least_percent / 100)
				# print(at_least_decimal)
			num_picks = len(betslip)

			if at_least_decimal > 1.99:
				at_least_moneyline = round((at_least_decimal - 1) * 100, 2)
				print(f"Odds for At Least 1 Event to Occur Out of {num_picks} are: {plus}{at_least_moneyline}")
				print(f"Percent Chance for At Least 1 Event to Occur Out of {num_picks} are: {at_least_percent}%")
				wager = int(input("How Much Would you Like to Wager?: $"))
				to_win = round(at_least_moneyline * (wager / 100))
				payout = round(to_win + wager, 2)
				print(f"Wager: ${wager} Odds: {plus}{at_least_moneyline} To Win: ${to_win}")
				print(f"Potential Payout: ${payout}")
				print("\n")
			elif at_least_decimal <= 1.99:
				at_least_moneyline = round(-100 / (at_least_decimal - 1))
				print(f"Odds for At Least 1 Event to Occur Out of {num_picks} are: {at_least_moneyline}")
				print(f"Percent Chance for At Least 1 Events to Occur Out of {num_events} are: {at_least_percent}%")
				wager = int(input("How Much Would you Like to Wager?: $"))
				to_win = round((at_least_decimal - 1) * 100)
				payout = round(to_win + wager)
				print(f"Wager: ${wager} Odds: {at_least_moneyline} To Win: ${to_win}")
				print(f"Potential Payout: ${payout}")
				print("\n")
		elif options == "At Least 2":
			"""P(at least two successes) = 1 - P(zero successes) - P(one success)"""
			"""P(X=k) = nCk * pk * (1-p)n-k"""
			""" n: number of trials
				k: number of successes
				p: probability of success on a given trial
				nCk: the number of ways to obtain k successes in n trials """
			# print(decimal_odds)
			if num_events == 3:
				outcome_a = decimal_odds[0]
				outcome_b = decimal_odds[1]
				outcome_c = decimal_odds[2]
				percent_a = round((1 / outcome_a), 2)
				percent_b = round((1 / outcome_b), 2)
				percent_c = round((1 / outcome_c), 2)
				prob_of_none = (1 - percent_a) * (1 - percent_b) * (1 - percent_c)
				prob_of_a = percent_a * (1 - percent_b) * (1 - percent_c)
				prob_of_b = percent_b * (1 - percent_a) * (1 - percent_c)
				prob_of_c = percent_c * (1 - percent_a) * (1 - percent_b)
				prob_of_one = prob_of_a + prob_of_b + prob_of_c
				at_least_2 = 1 - prob_of_none - prob_of_one
				p2 = round(at_least_2 * 100, 1)
				p2_decimal = 1 / (p2 / 100)
			elif num_events == 4:
				outcome_a = decimal_odds[0]
				outcome_b = decimal_odds[1]
				outcome_c = decimal_odds[2]
				outcome_d = decimal_odds[3]
				percent_a = round((1 / outcome_a), 2)
				percent_b = round((1 / outcome_b), 2)
				percent_c = round((1 / outcome_c), 2)
				percent_d = round((1 / outcome_d), 2)

				prob_of_none = (1 - percent_a) * (1 - percent_b) * (1 - percent_c) * (1 - percent_d)
				# print(f"Prob of none: {prob_of_none}")

				prob_of_a = percent_a * (1 - percent_b) * (1 - percent_c) * (1 - percent_d)
				# print(prob_of_a)
				prob_of_b = percent_b * (1 - percent_a) * (1 - percent_c) * (1 - percent_d)
				# print(prob_of_b)
				prob_of_c = percent_c * (1 - percent_a) * (1 - percent_b) * (1 - percent_d)
				# print(prob_of_c)
				prob_of_d = percent_d * (1 - percent_a) * (1 - percent_b) * (1 - percent_c)
				# print(prob_of_d)

				prob_of_one = prob_of_a + prob_of_b + prob_of_c + prob_of_d
				# print(f"Prob of one: {prob_of_one}")

				at_least_2 = 1 - prob_of_none - prob_of_one
				p2 = round(at_least_2 * 100, 1)
				p2_decimal = 1 / (p2 / 100)
			# print(p2_decimal)
			# print(f"Prob of at least 2: {p2}")
			if p2_decimal > 1.99:
				p2_moneyline = round((p2_decimal - 1) * 100, 2)
				print(f"Odds for At Least 2 Events to Occur Out of {num_events} are: {plus}{p2_moneyline}")
				print(f"Percent Chance for At Least 2 Events to Occur Out of {num_events} are: {p2}%")
				wager = int(input("How Much Would you Like to Wager?: $"))
				to_win = round(p2_moneyline * (wager / 100))
				payout = round(to_win + wager, 2)
				print(f"Wager: ${wager} Odds: {plus}{p2_moneyline} To Win: ${to_win}")
				print(f"Payout: ${payout}")
				print("\n")
			elif p2_decimal <= 1.99:
				p2_moneyline = round(-100 / (p2_decimal - 1))
				print(f"Odds for At Least 2 Events to Occur Out of {num_events} are: {p2_moneyline}")
				print(f"Percent Chance for At Least 2 Events to Occur Out of {num_events} are: {p2}%")
				wager = int(input("How Much Would you Like to Wager?: $"))
				to_win = round((p2_decimal - 1) * 100)
				payout = round(to_win + wager)
				print(f"Wager: ${wager} Odds: {p2_moneyline} To Win: ${to_win}")
				print(f"Potential Payout: {payout}")
				print("\n")
