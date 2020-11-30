order_in = [[34587, 'Learning Python, Mark Lutz', 4, 40.95],
            [98762, 'Programming Python, Mark Lutz', 5, 56.80],
            [77226, 'Head First Python, Paul Barry', 3, 32.95],
            [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]]
cost = lambda tmp: (tmp[0], round((tmp[len(tmp)-2] * tmp[len(tmp)-1]) if (tmp[len(tmp)-2] * tmp[len(tmp)-1]) > 100 else ((tmp[len(tmp)-1] + 10) * tmp[len(tmp)-2]), 2))
reform = lambda temp: tuple(temp)
order_out = list(map(cost, order_in))
print(order_out)
