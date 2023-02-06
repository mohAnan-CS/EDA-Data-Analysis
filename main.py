from database import Connector, DataBaseCreator, DataBaseTables
from file_operation import ReadData, StoreDataDataBase

connection = Connector.connect("root", "localhost", "0000")
database_cursor = connection.cursor()
# database_cursor.execute("DROP DATABASE SalesDataBase;")
# DataBaseCreator.create_database(database_cursor, "SalesDataBase")
# database_cursor.execute("USE SalesDataBase")
# DataBaseTables.create_tables(database_cursor)

# database_cursor.execute("SHOW TABLES")
#
# for table_name in database_cursor:
#     print(table_name)

# ----------------- Read data files ----------------------

# ReadData.read_customer_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\customer.csv")
# ReadData.read_product_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\product.csv")
ReadData.read_sales_outlet_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\sales_outlet.csv")

# StoreDataDataBase.store_customer(data_customer)
