from sqlalchemy import create_engine

def test_connection(server_address, database_name):
    # Construct the connection string
    conn_str = f'mssql+pyodbc://{server_address}/{database_name}?trusted_connection=yes'
    
    try:
        # Try connecting to the server
        engine = create_engine(conn_str)
        connection = engine.connect()
        connection.close()
        print("Connection successful!")
    except Exception as e:
        print(f"Error connecting to the server: {e}")

if __name__ == "__main__":
    server_address = 'your_server_address'
    database_name = 'your_database_name'
    
    test_connection(server_address, database_name)
