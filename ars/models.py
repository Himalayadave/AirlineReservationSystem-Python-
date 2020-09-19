import random
import datetime
from datetime import date


# Dict to maintain data (Consider them as db)
users = {}
flights = {}
bookings = {}


class Customer:
    def __init__(self, username, name, age, email, password):
        self.username = username
        self.name = name
        self.age = age
        self.email = email
        self.password = password
        self.booking_history = []

    def customer_detail(self):
        return (self.name, self.age, self.email)


class Flight:

    FLIGHT_CLASS = (
        "First Class",
        "Business Class",
        "Premium Economy",
        "Economy",
    )

    def __init__(
        self,
        flight_id,
        aircraft_type,
        source,
        destination,
        stops,
        departure,
        arrival,
        totaltime,
    ):
        self.flight_id = flight_id
        self.aircraft_type = aircraft_type
        self.source = source
        self.destination = destination
        self.seats = {
            self.FLIGHT_CLASS[0]: 50,
            self.FLIGHT_CLASS[1]: 50,
            self.FLIGHT_CLASS[2]: 100,
            self.FLIGHT_CLASS[3]: 150,
        }
        self.price = {
            self.FLIGHT_CLASS[0]: 14500,
            self.FLIGHT_CLASS[1]: 12000,
            self.FLIGHT_CLASS[2]: 8800,
            self.FLIGHT_CLASS[3]: 5500,
        }
        self.stops = stops
        self.departure = departure
        self.arrival = arrival
        self.totaltime = totaltime

    def get_flight_detail(self):
        return (
            self.flight_id,
            self.aircraft_type,
            self.source,
            self.destination,
            self.seats,
            self.price,
            self.stops,
            self.departure,
            self.arrival,
            self.totaltime,
        )

    def seat_availability(self, **kwargs):
        booking_class = kwargs["booking_class"]
        flight = kwargs["flight"]
        quantity = kwargs["quantity"]
        if (
            flight.seats[booking_class] != 0
            and flight.seats[booking_class] >= quantity
        ):
            return True
        else:
            return False

    def update_seat_status(
        self, quantity, flight, booking_class, payment_status
    ):
        self.quantity = quantity
        self.flight = flight
        self.booking_class = booking_class
        self.payment_status = payment_status
        flight.seats[booking_class] -= quantity

    @classmethod
    def flight_search(self, source, destination):
        self.source = source
        self.destination = destination
        for i in flights.keys():
            flight = flights[i]
            if source == flight.source and destination == flight.destination:
                return flight

    def flight_delete(self, id):
        del flights[id]


class Payment:
    @classmethod
    def payment_status(self):
        return True


class Booking:
    def __init__(
        self,
        booking_id,
        pnr,
        booking_time,
        payment,
        customer,
        passengers,
        flight,
    ):
        self.booking_id = booking_id
        self.pnr = pnr
        self.booking_time = booking_time
        self.payment = payment
        self.customer = customer
        self.passengers = passengers
        self.flight = flight

    @classmethod
    def create_reservation(self, **kwargs):
        seat_availability = kwargs["seat_availability"]
        customer = kwargs["customer"]
        quantity = kwargs["quantity"]
        if seat_availability:
            booking_class = kwargs["booking_class"]
            flight = kwargs["flight"]
            payment = flight.price[booking_class] * quantity
            flight.update_seat_status(
                quantity, flight, booking_class, Payment.payment_status
            )
            booking_id = "BOID" + str(random.randrange(10, 100000, 2))
            pnr = "PNR" + str(random.randrange(10, 10000000, 2))
            booking_time = datetime.datetime.now()
            passengers = []

            while quantity > 0:
                quantity -= 1
                names = input()
                passengers.append(names)
            booking = Booking(
                booking_id,
                pnr,
                booking_time,
                payment,
                customer,
                passengers,
                flight,
            )
            bookings[pnr] = booking
            customer.booking_history.append(booking)
            return booking

    def get_booking_detail(self):
        return (
            self.booking_id,
            self.pnr,
            self.booking_time.strftime("%Y-%m-%d %H:%M:%S"),
            f"₹{str(self.payment)}",
            self.passengers,
            self.customer.username,
            self.flight.flight_id,
        )
