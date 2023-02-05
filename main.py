from database import Connector, DataBaseCreator, DataBaseTables

connection = Connector.connect("root", "localhost", "0000")
database_cursor = connection.cursor()
# database_cursor.execute("DROP DATABASE SalesDataBase;")
# DataBaseCreator.create_database(database_cursor, "SalesDataBase")
database_cursor.execute("USE SalesDataBase")
# DataBaseTables.create_tables(database_cursor)

database_cursor.execute("SHOW TABLES")

for table_name in database_cursor:
    print(table_name)
