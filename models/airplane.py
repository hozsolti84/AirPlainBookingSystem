class Airplane:
    def __init__(self, model: str, registration: str, capacity: int):
        """
        model: str (e.g., “Airbus A320”)
        registration: str (tail number)
        capacity: int
        """
        self.model = model
        self.registration = registration
        self.capacity = capacity