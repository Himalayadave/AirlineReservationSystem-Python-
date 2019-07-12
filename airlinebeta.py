import random
import datetime
from datetime import date

users={}
flights={}
bookings={}

class Customer:
    def __init__(self,username,name,age,email,password):
        self.username=username
        self.name=name
        self.age=age
        self.email=email
        self.password=password
        self.booking_history=[]
        
    def customerDetails(self):
        return(self.name,self.age,self.email)

class Booking:
    def __init__(self,booking_id,pnr,booking_time,payment,customer,passengers,
                 flight):
        self.booking_id=booking_id
        self.pnr=pnr
        self.booking_time=booking_time
        self.payment=payment
        self.customer=customer
        self.passengers=passengers
        self.flight=flight
    
    @classmethod
    def make_reservation(self,**kwargs):
        availability_status = kwargs['availability_status']
        customer = kwargs['customer']
        quantity = kwargs['quantity']
        if availability_status:
            booking_class = kwargs['booking_class']
            airline = kwargs['airline']
            payment=airline.price[booking_class] * quantity   
            airline.seat_status(quantity,airline,booking_class,Payment.payment_status)
            booking_id = "BOID" + str(random.randrange(10,100000,2))
            pnr = "PNR" + str(random.randrange(10,10000000,2))
            booking_time = datetime.datetime.now()
            passengers = []
            while quantity>0:
                quantity-=1
                names=input()
                passengers.append(names)
            booking=Booking(booking_id,pnr,booking_time,payment,customer,passengers,airline)
            bookings[pnr]=booking
            customer.booking_history.append(booking)
            return(booking)

    def booking_details(self):
        return(self.booking_id,self.pnr,self.booking_time.strftime("%Y-%m-%d %H:%M:%S"),"₹"+ str(self.payment),
               self.passengers,self.customer.username,self.flight.flight_id)

class Flight:
    
    flight_classes = ('First Class','Business Class','Premium Economy','Economy')
    
    def __init__(self,flight_id,aircraft_type,source,destination,stops,
                 departure,arrival,totaltime):
        self.flight_id=flight_id
        self.aircraft_type=aircraft_type
        self.source=source
        self.destination=destination
        self.seats = { self.flight_classes[0] : 50,
                       self.flight_classes[1] : 50,
                       self.flight_classes[2] : 100,
                       self.flight_classes[3] : 150
                     }
        self.price = { self.flight_classes[0] : 14500,
                       self.flight_classes[1] : 12000,
                       self.flight_classes[2] : 8800,
                       self.flight_classes[3] : 5500
                     }  
        self.stops=stops
        self.departure=departure
        self.arrival=arrival
        self.totaltime=totaltime  

    def flight_details(self):
        return(self.flight_id,self.aircraft_type,self.source,self.destination,self.seats,self.price,
               self.stops,self.departure,self.arrival,self.totaltime)

    def seat_availability(self,**kwargs):
        booking_class = kwargs['booking_class']
        airline = kwargs['airline']
        quantity = kwargs['quantity']
        if airline.seats[booking_class] != 0 and airline.seats[booking_class] >= quantity:
            return True
        else:
            return False

    def seat_status(self,quantity,flight,booking_class,payment_status):
        self.quantity=quantity
        self.flight=flight
        self.booking_class=booking_class
        self.payment_status=payment_status
        flight.seats[booking_class]-=quantity
    
    @classmethod
    def flight_search(self,source,destination):
        self.source=source
        self.destination=destination
        for i in flights.keys():
            flight=flights[i]
            if source==flight.source and destination==flight.destination:
                return flight 
    
    def delete_flight(self,flight_id):
        del flights[flight_id]
        
class Payment:
    @classmethod
    def payment_status(self):
        return True
    
    
#--------------------------------------------------------StaticDemo--------------------------------------------------    
#FlightInstance         
airline1 = Flight("DOXIN" + str(random.randrange(10,100000,2)),"Boeing 777","INDORE","GOA",0,"3pm","6pm",3)
flights["DOXIN" + str(random.randrange(10,100000,2))]=airline1

#CustomerInstance
customer1 = Customer("usernamegamma","namecharlie",10,"emailalpha","passworddelta")
users["username"]=customer1

#SearchFunctionality
flight=Flight.flight_search("INDORE","GOA")
print(flight.flight_details()) 

#CheckingAvailability
availability = flight.seat_availability(airline = flight, booking_class = flight.flight_classes[0] ,quantity=2)

#MakingReservation
status=Booking.make_reservation(airline = flight ,booking_class = flight.flight_classes[0],customer=customer1,availability_status=availability,quantity=2)

#ReturningBookingObjectandGettingDetails
print(status.booking_details())
