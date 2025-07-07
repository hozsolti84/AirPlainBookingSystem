
from repos.airplane_repo import AirplaneRepo

class Airplane:
    def __init__(self,
                 model: str=None,
                 registration: str=None,
                 capacity: int=None):
        """
        model: str (e.g., “Airbus A320”)
        registration: str (tail number)
        capacity: int
        """
        self.__model = model
        self.__registration = registration
        self.__capacity = capacity

    def check_airplane(self, registration=None):
        if registration:
            # registration = self.registration
            airplane = AirplaneRepo()
            data = airplane.get_by_id(registration=registration)
            return data

    def add_airplane(self, model, registration, capacity):
        exists = self.check_airplane(registration=registration)
        if not exists:
            print("The airplane will be created!")
            self.__model = model
            self.__registration = registration
            self.__capacity = capacity
            airplane = AirplaneRepo()
            airplane.add(model=model, registration=registration, capacity=capacity)
        else:
            print("The airplane already exists!")

    def remove_airplane(self, model, registration, capacity):
        exists = self.check_airplane(registration=registration)
        if not exists:
            print("The airplane will be created!")
            self.__model = model
            self.__registration = registration
            self.__capacity = capacity
            airplane = AirplaneRepo()
            airplane.delete(model=model, registration=registration, capacity=capacity)
        else:
            print("The airplane DOES NOT exist!")




if __name__=='__main__':
    airplane = Airplane()
    """check_airplane() test"""
    # airplane_data = airplane.check_airplane("HA-LYA")
    # airplane_data = airplane.check_airplane("H-LYA")
    # if airplane_data:
    #     print(airplane_data)
    # else:
    #     print("Airplane not found!")

    """add_airplane"""
    # airplane.add_airplane("SuperWing", "11", 1)
    airplane.remove_airplane('XWing', "'qwer'", 1)















