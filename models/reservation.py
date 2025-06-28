from datetime import datetime
from models.person import Passenger
from models.flight import Flight


class Reservation:
    def __init__(self, reservation_id: str, passenger: Passenger, flight: Flight, seat_number: str, status: str,
                 booking_time: datetime):
        self.reservation_id = reservation_id
        self.passenger = passenger
        self.flight = flight
        self.seat_number = seat_number
        self.status = status
        self.booking_time = booking_time

    def cancel(self):
        """ updates status, removes from passenger and flight records"""
        pass

    def summary(self):
        """ returns printable reservation details """
        pass