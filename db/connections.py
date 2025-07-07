# project/repos/people.py
import mysql.connector
import config

class CreateConnection:
    def create_connection(self):
        connection = mysql.connector.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        return connection



if __name__ == "__main__":
    print("Connecting with:")
    print(f"Host: {config.DB_HOST}, "
          f"Port: {config.DB_PORT}, "
          f"User: {config.DB_USER}, "
          f"DB: {config.DB_NAME}")

    connector = CreateConnection()
    connection = connector.create_connection()
    if connection and connection.is_connected():
        print("Connection to MySQL database was successful!")
        connection.close()
    else:
        print("Failed to connect to the MySQL database.")