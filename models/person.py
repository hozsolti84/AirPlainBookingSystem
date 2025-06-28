from abc import ABC, abstractmethod
from models.reservation import Reservation
from models.flight import Flight


class Person(ABC):
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
class Passenger(Person):
    def __init__(self, name, email, passport_number: str, frequent_flyer_points: str = 0):
        """
        passport_number: str
		frequent_flyer_points: int (default: 0)
        reservations: list of Reservation objects (composition)
        """
        super().__init__(name, email)
        self.passport_number = passport_number
        self.frequent_flyer_points = frequent_flyer_points
        self.reservations = []

    def book_flight(self, flight: Flight, seat_number: str) -> Reservation:
        pass

    def cancel_reservation(self, reservation_id: str):
        pass


class Employee(Person):
    def __init__(self, name, email, employee_id: str, role: str):
        super().__init__(name, email)
        self.employee_id = employee_id
        self.role = role


