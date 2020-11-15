import mysql.connector
import database_config as cfg
from database_config import config_string


DATABASE_CONNECTION_STRING = cfg.read_db_config()


def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(user=DATABASE_CONNECTION_STRING['mysql']['user'],
                                             host=DATABASE_CONNECTION_STRING['mysql']['host'],
                                             port=DATABASE_CONNECTION_STRING['mysql']['port'],
                                             password=DATABASE_CONNECTION_STRING['mysql']['password'],
                                             database=DATABASE_CONNECTION_STRING['mysql']['database'])
    except Exception as error:
        print("Error while connecting to database for job tracker", error)
    return connection


def main():
    conn = get_db_connection()


if __name__ == "__main__":
    main()
