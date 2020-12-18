from pprint import pprint
def get_data():
    tickets = [ticket.split(',') for ticket in open('other_tickets.txt', 'r').read().strip().split('\n')]
    tickets_num = [[int(x) for x in ticket] for ticket in tickets]
    myticket = [int(x) for x in open('myticket.txt','r').readline().strip().split(',')]
    d = {}
    with open('fields_ranges.txt', 'r') as file:
        files = file.read().strip().split('\n')
    for line in files:
        field_name, text = line.split(':')
        range1, range2 = text.split('or')
        start1, stop1 = range1.split('-')
        start1 = int(start1.strip())
        stop1 = int(stop1.strip())
        start2, stop2 = range2.split('-')
        start2 = int(start2.strip())
        stop2 = int(stop2.strip())
        d[field_name] = [[start1, stop1], [start2, stop2]]
    return myticket, tickets_num, d

def det_invalid(rule, first, last, value):
    """tests value to see if """

myticket, tickets, field_rules = get_data()
pprint(field_rules)
