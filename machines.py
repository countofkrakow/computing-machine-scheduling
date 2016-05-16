from data import parse_file

# determines how much money this machine would earn if run to the end
def net_profit(machine, time):
    net = machine['profit_rate'] * time + machine['resale_price'] - machine['purchase_price']
    return net

def max(case):
    empty_machine = {
        'day': 0,
        'purchase_price': 0,
        'resale_price': 0,
        'profit_rate': 0
    }

    return choose(empty_machine, case['C'], case['machines'], case['D'])

def choose(curr_machine, money, available_machines, total_days):
    curr_day = curr_machine['day']

    # base case:
    if not available_machines:
        return money + curr_machine['resale_price'] + (total_days - curr_day) * curr_machine['profit_rate']

    else:
        best_profit = choose(curr_machine, money, [], total_days)

        for machine in available_machines:
            next_day = machine['day']
            can_afford = money + curr_machine['resale_price'] + curr_machine['profit_rate'] \
                         * (next_day - curr_day - 1) >= machine['purchase_price']
            net_positive = net_profit(machine, total_days - next_day) > 0

            if (can_afford and net_positive):
                next_money = money + curr_machine['resale_price'] - machine['purchase_price'] + \
                             curr_machine['profit_rate'] * (next_day - curr_day - 1)

                next_machines = [x for x in available_machines if x['day'] > next_day]
                profit = choose(machine, next_money, next_machines, total_days)
                if profit > best_profit:
                    best_profit = profit
        return best_profit

def main():
    data = parse_file()
    for i, case in enumerate(data):
        result = max(case)
        print("Case %d: %d" % (i, result))

if __name__ == '__main__':
    main()