#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    trip={}

    for ticket in tickets:
        trip[ticket.source] = ticket.destination

    next_stop = trip['NONE']
    
    route = []
    for i in range(length):
       route.append(next_stop)
       next_stop = trip[next_stop]
    
    return route


# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]

# expected = ["PDX", "DCA", "NONE"]

# print(reconstruct_trip(tickets, 3))