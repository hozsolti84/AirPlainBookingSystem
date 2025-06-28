# project/repos/people.py
import mysql.connector
import config

class CreateConnection:
    def get_connection(self):
        return mysql.connector.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )

    def create_connection(self):
        pass