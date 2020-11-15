import pandas as pd
import os
from database_connection import get_db_connection


FILE_NAME = 'third_party_sales_1.csv'
DIR_PATH = 'Event_Ticket_System_Data_Pipeline/data/'
FILE_PATH = os.path.join(os.environ['HOME'], DIR_PATH, FILE_NAME)

conn = get_db_connection()


def read_csv(file_path):
    df = pd.read_csv(file_path, header=None)
    return df


def load_third_party(connnection):
    cursor = connnection.cursor()
    data = read_csv(FILE_PATH)
    for _, row in data.iterrows():
        sql = "INSERT INTO ticket_sales VALUES (" + "%s,"*(len(row)-1) + "%s)"
        try:
            cursor.execute(sql, tuple(row))
        except Exception as error:
            print(error)
    connnection.commit()
    cursor.close()
    return


def main():
    load_third_party(conn)


if __name__ == "__main__":
    main()
