class Flights:
    counter = 1
    def __init__(self, origin, destination, duration):

        self.id =Flights.counter
        Flights.counter += 1

        self.origin = origin
        self.destination = destination
        self.duration = duration

        self.passengers = []

    def add_passenger(self,p):
        self.passengers.append(p)
        p.flight_id = self.id

class passengers:
    def __init__(self, name):
        self.name = name

def main():
    f1 = Flights("HUE", "SG", 90)
    f2 = Flights("HUE", "HN", 60)

    p1 = passengers("vu")
    p2 = passengers("tien")
    p3 = passengers("the")

    f1.add_passenger(p1)
    f1.add_passenger(p2)
    f2.add_passenger(p3)

    print(len(f1.passengers), len(f2.passengers))

    for passenger in f1.passengers:
        print(passenger.name)

    print(p1.flight_id, p2.flight_id, p3.flight_id)

if __name__ == "__main__":
    main()
