from database import Connector
from file_operation import ReadCustomer, ReadProduct, ReadSalesOutlet, ReadSalesTarget
from database.storing import StoreCustomer, StoreProduct

connection = Connector.connect("root", "localhost", "0000")
database_cursor = connection.cursor()
# database_cursor.execute("DROP DATABASE SalesDataBase;")
# DataBaseCreator.create_database(database_cursor, "SalesDataBase")
database_cursor.execute("USE SalesDataBase")
# DataBaseTables.create_tables(database_cursor)

# database_cursor.execute("SHOW TABLES")
#
# for table_name in database_cursor:
#     print(table_name)

# ----------------- Read data files ----------------------

# customer_list = ReadCustomer.read_customer_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\customer.csv")
product_list = ReadProduct.read_product_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\product.csv")
print(product_list)
# ReadSalesOutlet.read_sales_outlet_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\sales_outlet.csv")
# ReadSalesTarget.read_sales_target_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\sales targets.csv")

# ------------------ Store data files ---------------------
# StoreCustomer.store_all(customer_list, database_cursor, connection)
StoreProduct.store_all(product_list, database_cursor, connection)
