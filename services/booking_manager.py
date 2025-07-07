from models.airplane import Airplane
from models.person import Passenger
from models.flight import Flight
from models.reservation import Reservation
from errors.errors import SeatAlreadyBookedError

class BookingManager:
    """
        ○ Handles reservation creation and cancellation
		○ Ensures airplane and seat consistency
		○ Prevents invalid operations (e.g., double-booking)
    """

    def __init__(self, reservation=None):
        self.__airplane = Airplane()
        self.__reservations = reservation if reservation is not None else []

    def create_airplane(self, model, registration, capacity):
        self.__airplane.add_airplane(model=model, registration=registration, capacity=capacity)

    def get_airplane(self, registration):
        self.__airplane.check_airplane(registration=registration)

    def remove_airplane(self, model, registration, capacity):
        self.__airplane.remove_airplane(model, registration, capacity)

    def create_flight(self):
        pass

    def get_fligth(self):
        pass

    def cancel_flight(self):
        pass



    def create_reservation(self, passenger: Passenger, flight: Flight, seat_number: str) -> Reservation:
        pass

    def cancel_reservation(self, reservation_id: str):
        pass

    def list_flight_reservations(self, flight_number: str) -> list[Reservation]:
        pass

    def check_bookings(self):
        """
        If a seat on a flight is already booked by one passenger, the system must not allow another passenger to
        reserve the same seat on that same flight.
        """
        try:
            pass
        except SeatAlreadyBookedError as e:
            print(e)
