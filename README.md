## Event Ticket System Data Pipeline
Run the shell script to ingest data into MySQL database and return the top three ticket sellers.
<br/><br/>
Two ways to run the program.
- ticket_sales.sh
- cherry-pick.sh
<br/><br/>
### ticket_sales.sh
```shell
bash ticket_sales.sh
```
to generate config file, establish database connection, ingest data and analyze top sellers.
<br/><br/>
### cherry-pick.sh

*For example:*
```shell
bash cherry-pick.sh scripts/database_connection.py scripts/analyze_ticket_sales.py
```
to skip creating config file and loading data again into the table.
