
from db.connections import CreateConnection
from utils.basic import get_data
class AirplaneRepo:
    # todo: This should not be here. It should be in the config.py.
    path = r"C:\Users\A87484215\intermediatePythonKnowledge\AirPlainBookingSystem\db\queries.ini"
    section = "airplane"

    def __init__(self, model=None, registration=None, capacity=None):
        self.__model = model
        self.__registration = registration
        self.__capacity = capacity
        self.__connector = CreateConnection()
        self.__connection = self.__connector.create_connection()
        # todo: This check should be somewhere else, Exception maybe?
        if self.__connection and self.__connection.is_connected():
            print("Connection to MySQL database was successful!")
        else:
            print("Failed to connect to the MySQL database.")

    def get_query(self, action="select"):
        query = get_data(AirplaneRepo.path, AirplaneRepo.section, action)
        print("The base query is: ", query)
        return query

    def execute_query(self, action, model=None, registration=None, capacity=None):
        query = AirplaneRepo.get_query(self, action=action)
        if action == "select":
            params = (registration,)
        else:
            params = (model, registration, capacity)
        with self.__connection.cursor() as cursor:
            cursor.execute(query, params=params)
            if action == "select":
                result = cursor.fetchall()
            else:
                self.__connection.commit()
                if cursor.rowcount > 1:
                    result = "OK"
                else:
                    result = "Not OK"
            return result

    def get_by_id(self, registration):
        result = AirplaneRepo.execute_query(self, action="select", registration=registration)
        if result:
            for res in result:
                print(res)
        else:
            print("No result was found!")

    def add(self, model, registration, capacity, action="insert"):
        print("Add was called!")
        AirplaneRepo.execute_query(self, action=action, model=model, registration=registration, capacity=capacity)


    def delete(self, model, registration, capacity, action="delete"):
        print(f"The airplane {model}, {registration}, {capacity}")
        AirplaneRepo.execute_query(self, action=action, model=model, registration=registration, capacity=capacity)



if __name__=="__main__":
    airplane = AirplaneRepo()
    airplane.get_by_id("HA-LYA")
    airplane.add(model="XWing", registration="qwer", capacity=1)