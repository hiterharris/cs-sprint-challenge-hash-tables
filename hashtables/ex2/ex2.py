#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    ticket_dict = {}
    route = [None] * (len(tickets))
    for ticket in tickets:
        if ticket.source == "NONE":
            route[0] = ticket.destination
        ticket_dict[ticket.source] = ticket.destination

    for i in range(1, len(tickets)):
        route[i] = ticket_dict[route[i-1]]
    print(ticket_dict)
    print(route)

    return route
