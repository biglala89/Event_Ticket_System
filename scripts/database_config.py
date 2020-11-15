import json

config_string = {
    'mysql': {
        'user': 'root',
        'host': 'localhost',
        'port': '3306',
        'password': '<your password goes here>',
        'database': 'ticket_sales',
    }
}


def create_db_config(data):
    with open('db_config.json', 'w') as output_file:
        json.dump(data, output_file)


def read_db_config():
    with open('db_config.json', 'r') as json_file:
        data = json.load(json_file)
    return data


def main():
    create_db_config(config_string)


if __name__ == '__main__':
    main()
