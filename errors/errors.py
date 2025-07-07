class SeatAlreadyBookedError(Exception):
    def __init__(self, message="The seat is already booked."):
        self.message=message