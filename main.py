import random
from ars.models import Customer, Booking, Flight, Payment
from ars.models import users, flights, bookings


def main():
    # Create a flight instance.
    flight_instance = Flight(
        "DOXIN" + str(random.randrange(10, 100000, 2)),
        "Boeing 777",
        "INDORE",
        "GOA",
        0,
        "3pm",
        "6pm",
        3,
    )
    # Storing flight in the dict.
    flights["flight"] = flight_instance
    print("*****FLIGHT INSTANCE*****", flight_instance)

    # Create customer instance.
    customer_instance = Customer(
        "usernamegamma", "namecharlie", 10, "emailalpha", "passworddelta"
    )
    # Storing customer in the dict. Storing with username for unique record.
    users["customer"] = customer_instance
    print("*****CUSTOMER INSTANCE*****", customer_instance)

    # Search flight
    flight = Flight.flight_search("INDORE", "GOA")
    print("*****FLIGHT DETAIL*****", flight.get_flight_detail())

    # Check seat availability in the flight.
    seat_availability = flight.seat_availability(
        flight=flight, booking_class=flight.FLIGHT_CLASS[0], quantity=2
    )
    print("*****SEAT AVAILABILITY*****", seat_availability)

    # Create reservation
    booking_instance = Booking.create_reservation(
        flight=flight,
        booking_class=flight.FLIGHT_CLASS[0],
        customer=customer_instance,
        seat_availability=seat_availability,
        quantity=2,
    )
    print("*****BOOKING INSTANCE*****", booking_instance)

    # Get booking info
    print("*****BOOKING DETAIL*****", booking_instance.get_booking_detail())


main()
