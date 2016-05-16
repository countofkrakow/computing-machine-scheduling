# parses input

filename = "input.txt"

def parse_file(name=filename):
    cases = []
    f = open(name , 'r')
    line = f.readline()
    while line:
        line_arr = line.split()

        # add an empty case to the cases list
        if len(line_arr) == 3:
            case = {'machines': []}
            case['N'] = int(line_arr[0])
            case['C'] = int(line_arr[1])
            case['D'] = int(line_arr[2])
            cases.append(case)

        # append a machine to the most recent case
        elif len(line_arr) == 4:
            machine = {
                'day': int(line_arr[0]),
                'purchase_price': int(line_arr[1]),
                'resale_price': int(line_arr[2]),
                'profit_rate': int(line_arr[3])
            }
            cases[-1]['machines'].append(machine)
        else:
            print('There was an error parsing the input file. Exiting...')
            exit(1)

        line = f.readline()
    return cases