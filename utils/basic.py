from configparser import ConfigParser

def get_data(path, section, key):
    parser = ConfigParser()
    parser.read(path)
    value = parser.get(section, key, fallback="The data was not found.")
    print(value)
    return value



if __name__=='__main__':
    """test for get_data()"""
    # path = r"C:\Users\A87484215\intermediatePythonKnowledge\AirPlainBookingSystem\db\queries.ini"
    path = r"C:\Users\A87484215\intermediatePythonKnowledge\AirPlainBookingSystem\db\queries.ini"
    get_data(path, "airplane", "select")
