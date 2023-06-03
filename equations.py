import colorama
from colorama import Fore


class Options:

	def __init__(self, decimal_odds, betslip, plus, num_events):

		def as_currency(amount):
			if amount >= 0:
				return '${:,.2f}'.format(amount)
			else:
				return '-${:,.2f}'.format(-amount)
		if num_events == 4:
			options = input("Bet Options:\nType '1' for 'At Least 1'\nType '2' for 'At Least 2'\nType '3' for 'Round Robin': ")
			print("\n")
		else:
			options = input("Choose a Option: (At Least 1/At Least 2): ")
			print("\n")

		if options == "1":
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
				print("\n")
				print(f"Odds for At Least 1 Event to Occur Out of {num_picks} are: {plus}{at_least_moneyline}")
				print(f"Percent Chance for At Least 1 Event to Occur Out of {num_picks} are: {at_least_percent}%")
				print("\n")
				print(f"Odds: {at_least_moneyline}")
				wager = int(input("How Much Would you Like to Wager?: $"))
				to_win = round(at_least_moneyline * (wager / 100), 2)
				to_win_as_money = as_currency(to_win)
				payout = round(to_win + wager, 2)
				payout_as_money = as_currency(payout)
				print(f"Wager: ${wager}\nOdds: {plus}{at_least_moneyline}\nTo Win: {to_win_as_money}")
				print(f"Potential Payout: {payout_as_money}")
				print("\n")
			elif at_least_decimal <= 1.99:
				at_least_moneyline = round(-100 / (at_least_decimal - 1))
				print("\n")
				print(f"Odds for At Least 1 Event to Occur Out of {num_picks} are: {at_least_moneyline}")
				print(f"Percent Chance for At Least 1 Events to Occur Out of {num_events} are: {at_least_percent}%")
				print("\n")
				print(f"Odds: {at_least_moneyline}")
				wager = int(input("How Much Would you Like to Wager?: $"))
				to_win = round((wager / at_least_moneyline) * -100, 2)
				to_win_as_money = as_currency(to_win)
				payout = round(to_win + wager, 2)
				payout_as_money = as_currency(payout)
				print(f"Wager: ${wager}\nOdds: {at_least_moneyline}\nTo Win: {to_win_as_money}")
				print(f"Potential Payout: {payout_as_money}")
				print("\n")

		elif options == "2":
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
				print("\n")
				print(f"Odds for At Least 2 Events to Occur Out of {num_events} are: {plus}{p2_moneyline}")
				print(f"Percent Chance for At Least 2 Events to Occur Out of {num_events} are: {p2}%")
				print("\n")
				print(f"Odds: {p2_moneyline}")
				wager = int(input("How Much Would you Like to Wager?: $"))
				to_win = round(p2_moneyline * (wager / 100), 2)
				to_win_as_money = as_currency(to_win)
				payout = round(to_win + wager, 2)
				payout_as_money = as_currency(payout)
				print(f"Wager: ${wager}\nOdds: {plus}{p2_moneyline}\nTo Win: {to_win_as_money}")
				print(f"Potential Payout: {payout_as_money}")
				print("\n")
			elif p2_decimal <= 1.99:
				p2_moneyline = round(-100 / (p2_decimal - 1))
				print("\n")
				print(f"Odds for At Least 2 Events to Occur Out of {num_events} are: {p2_moneyline}")
				print(f"Percent Chance for At Least 2 Events to Occur Out of {num_events} are: {p2}%")
				print("\n")
				print(f"Odds: {p2_moneyline}")
				wager = int(input("How Much Would you Like to Wager?: $"))
				to_win = round((wager / p2_moneyline) * -100, 2)
				to_win_as_money = as_currency(to_win)
				payout = round(to_win + wager, 2)
				payout_as_money = as_currency(payout)
				print(f"Wager: ${wager}\nOdds: {p2_moneyline}\nTo Win: {to_win_as_money}")
				print(f"Potential Payout: {payout_as_money}")
				print("\n")

		elif options == "3":
			if num_events == 4:
				outcome_a = decimal_odds[0]
				outcome_b = decimal_odds[1]
				outcome_c = decimal_odds[2]
				outcome_d = decimal_odds[3]

				prod_ab = outcome_a * outcome_b
				prod_ac = outcome_a * outcome_c
				prod_ad = outcome_a * outcome_d

				prod_bc = outcome_b * outcome_c
				prod_bd = outcome_b * outcome_d

				prod_cd = outcome_c * outcome_d

				total_risk = 0.00
				max_win = 0.00

				twos = round((prod_ab + prod_ac + prod_ad + prod_bc + prod_bd + prod_cd) / 6, 2)
				# print(twos)
				if twos > 1.99:
					twos_moneyline = round((twos - 1) * 100)
					print(Fore.LIGHTWHITE_EX + f"By 2s x6 Odds: +{twos_moneyline}")
					wager_twos = int(input("By 2s x6 Wager: $"))
					total_risk_twos = wager_twos * 6
					total_risk_twos_as_money = as_currency(total_risk_twos)
					red_text_risk_twos_as_money = (Fore.RED + f'By 2s x6 Risk: {total_risk_twos_as_money}')
					total_risk += total_risk_twos
					max_win_twos = (twos_moneyline * total_risk_twos) / 100
					max_win_twos_as_money = as_currency(max_win_twos)
					blue_text_max_win_twos_as_money = (Fore.BLUE + f'Potential Max Win: {max_win_twos_as_money}')
					max_win += max_win_twos
					print(f"{red_text_risk_twos_as_money}\n{blue_text_max_win_twos_as_money}")

				elif twos <= 1.99:
					twos_moneyline = round(-100 / (twos - 1))
					print(Fore.LIGHTWHITE_EX + f"By 2s x6 Odds: {twos_moneyline}")
					wager_twos = int(input("By 2s x6 Wager: $"))
					total_risk_twos = wager_twos * 6
					total_risk_twos_as_money = as_currency(total_risk_twos)
					red_text_risk_twos_as_money = (Fore.RED + f'By 2s x6 Risk: {total_risk_twos_as_money}')
					total_risk += total_risk_twos
					max_win_twos = (total_risk_twos / twos_moneyline) * -100
					max_win_twos_as_money = as_currency(max_win_twos)
					blue_text_max_win_twos_as_money = (Fore.BLUE + f'Potential Max Win: {max_win_twos_as_money}')
					max_win += max_win_twos
					print(f"{red_text_risk_twos_as_money}\n{blue_text_max_win_twos_as_money}")

				print("\n")
				prod_abc = outcome_a * outcome_b * outcome_c
				prod_abd = outcome_a * outcome_b * outcome_d
				prod_acd = outcome_a * outcome_c * outcome_d
				prod_bcd = outcome_b * outcome_c * outcome_d

				threes = round((prod_abc + prod_abd + prod_acd + prod_bcd) / 4, 2)
				# print(threes)

				if threes > 1.99:
					threes_moneyline = round((threes - 1) * 100)
					print(Fore.LIGHTWHITE_EX + f"By 3s x4 Odds: +{threes_moneyline}")
					wager_threes = int(input("By 3s x4 Wager: $"))
					total_risk_threes = wager_threes * 4
					total_risk_threes_as_money = as_currency(total_risk_threes)
					red_text_risk_threes_as_money = (Fore.RED + f'By 3s x4 Risk: {total_risk_threes_as_money}')
					total_risk += total_risk_threes
					max_win_threes = (threes_moneyline * total_risk_threes) / 100
					max_win_threes_as_money = as_currency(max_win_threes)
					blue_text_max_win_threes_as_money = (Fore.BLUE + f'Potential Max Win: {max_win_threes_as_money}')
					max_win += max_win_threes
					print(f"{red_text_risk_threes_as_money}\n{blue_text_max_win_threes_as_money}")

				elif threes <= 1.99:
					threes_moneyline = round(-100 / (threes - 1))
					print(Fore.LIGHTWHITE_EX + f"By 3s x4 Odds: +{threes_moneyline}")
					wager_threes = int(input("By 3s x4 Wager: $"))
					total_risk_threes = wager_threes * 4
					total_risk_threes_as_money = as_currency(total_risk_threes)
					red_text_risk_threes_as_money = (Fore.RED + f'By 3s x4 Risk: {total_risk_threes_as_money}')
					total_risk += total_risk_threes
					max_win_threes = (total_risk_threes / threes_moneyline) * -100
					max_win_threes_as_money = as_currency(max_win_threes)
					blue_text_max_win_threes_as_money = (Fore.BLUE + f'Potential Max Win: {max_win_threes_as_money}')
					max_win += max_win_threes
					print(f"{red_text_risk_threes_as_money}\n{blue_text_max_win_threes_as_money}")

				print("\n")

				parlay_abcd = round(outcome_a * outcome_b * outcome_c * outcome_d, 2)
				# print(parlay_abcd)
				if parlay_abcd > 1.99:
					parlay_moneyline = round((parlay_abcd - 1) * 100)
					print(Fore.LIGHTWHITE_EX + f"4 Leg Parlay Odds: +{parlay_moneyline}")
					wager_parlay = int(input("4 Leg Parlay Wager: $"))
					total_parlay_risk = wager_parlay * 1
					total_parlay_risk_as_money = as_currency(total_parlay_risk)
					red_text_risk_parlay_as_money = (Fore.RED + f'4 Leg Parlay Risk: {total_parlay_risk_as_money}')
					total_risk += total_parlay_risk
					to_win_parlay = round((parlay_moneyline / 100) * wager_parlay, 2)
					to_win_parlay_as_money = as_currency(to_win_parlay)
					blue_text_max_win_parlay_as_money = (Fore.BLUE + f'Potential Max Win: {to_win_parlay_as_money}')
					max_win += to_win_parlay
					print(f"{red_text_risk_parlay_as_money}\n{blue_text_max_win_parlay_as_money}")

				elif parlay_abcd <= 1.99:
					parlay_moneyline = round(-100 / (parlay_abcd - 1))
					print(Fore.LIGHTWHITE_EX + f"4 Leg Parlay Odds: +{parlay_moneyline}")
					wager_parlay = int(input("4 Leg Parlay Wager: $"))
					total_parlay_risk = wager_parlay * 1
					total_parlay_risk_as_money = as_currency(total_parlay_risk)
					red_text_risk_parlay_as_money = (Fore.RED + f'4 Leg Parlay Risk: {total_parlay_risk_as_money}')
					total_risk += total_parlay_risk
					to_win_parlay = (total_parlay_risk / parlay_moneyline) * -100
					to_win_parlay_as_money = as_currency(to_win_parlay)
					blue_text_max_win_parlay_as_money = (Fore.BLUE + f'Potential Max Win: {to_win_parlay_as_money}')
					max_win += to_win_parlay
					print(f"{red_text_risk_parlay_as_money}\n{blue_text_max_win_parlay_as_money}")

			print("\n")
			total_risk_as_money = as_currency(total_risk)
			red_text_total_risk_as_money = (Fore.RED + f'Total Round Robin Wager Amount: {total_risk_as_money}')
			max_win_total_as_money = as_currency(max_win)
			blue_text_max_win_total_as_money = (Fore.BLUE + f'Potential Max Round Robin Win: {max_win_total_as_money}')
			print(f"{red_text_total_risk_as_money}\n{blue_text_max_win_total_as_money}")

			print("\n")


