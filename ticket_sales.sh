# Create config file
pipenv run python scripts/database_config.py

# Establish MySQL connection
pipenv run python scripts/database_connection.py

# Load data into database
pipenv run python scripts/load_data.py

# Analyze ticket sales
pipenv run python scripts/analyze_ticket_sales.py
