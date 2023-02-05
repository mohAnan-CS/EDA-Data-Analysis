import DataBaseTables
import DataBaseCreator
from Connector import Connector


connection = Connector().connect("root", "localhost", "0000")
database_cursor = connection.cursor()
# database_cursor.execute("DROP DATABASE SalesDataBase;")
DataBaseCreator.create_database(database_cursor, "SalesDataBase")
database_cursor.execute("USE SalesDataBase")
DataBaseTables.create_customer_table(database_cursor)