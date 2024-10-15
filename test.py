import MySQLdb

try:
    connection = MySQLdb.connect(
        host="192.168.0.119",  # or the IP address of the MySQL server
        port=3306,         # default MySQL port
        user="root",
        passwd="limon123",
    )
    print("Connected to MySQL server successfully!")
    connection.close()
except MySQLdb.OperationalError as e:
    print(f"Error connecting to MySQL: {e}")
