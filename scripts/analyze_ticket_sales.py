from database_connection import get_db_connection


def query_popular_tickets(connection):
    # Get the top 3 popular ticket in the past month
    stmt = """
            WITH events AS (
                SELECT event_name, COUNT(*) AS num_events
                FROM ticket_sales.ticket_sales ts 
                GROUP BY event_name 
            ), 

            event_ranks AS (
                SELECT event_name, num_events,
					   RANK () OVER (ORDER BY num_events) AS event_rank
                FROM events
            )

            SELECT event_name, num_events
            FROM event_ranks
            WHERE event_rank <= 3
            ORDER BY event_rank DESC;
            """
    cursor = connection.cursor()
    cursor.execute(stmt)
    records = cursor.fetchall()
    cursor.close()
    return records


def display_results(query_results):
    formatted_string = list(
        map(lambda x: '- ' + str(x[0]) + ' ' + '(' + str(x[1]) + ')', query_results))
    print('Here are the top 3 popular tickets in the past month (number of purchases):')
    print('\n'.join(formatted_string))


def main():
    conn = get_db_connection()
    res = query_popular_tickets(conn)
    display_results(res)


if __name__ == '__main__':
    main()
