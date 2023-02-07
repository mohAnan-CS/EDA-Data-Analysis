from database import Connector
from file_reader import ReadCustomer, ReadProduct, ReadSalesOutlet, ReadSalesTarget, ReadTransaction
from database.storing import StoreCustomer, StoreProduct, StoresSalesOutlet, StoreSalesTarget

connection = Connector.connect("root", "localhost", "0000")
database_cursor = connection.cursor()
# database_cursor.execute("DROP DATABASE SalesDataBase;")
# DataBaseCreator.create_database(database_cursor, "SalesDataBase")
database_cursor.execute("USE SalesDataBase")
# DataBaseTables.create_tables(database_cursor)

# ----------------- Read data files ----------------------

# customer_list = ReadCustomer.read_customer_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\customer.csv")
# product_list = ReadProduct.read_product_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\product.csv")
# sales_outlet_list = ReadSalesOutlet.read_sales_outlet_file(
#   "C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\sales_outlet.csv")
# sales_target_list = ReadSalesTarget.read_sales_target_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\sales targets.csv")
transaction_list = ReadTransaction.read_transaction_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\201904 sales reciepts.csv")
print(transaction_list[0])
# ---------------------------------------------------------

# ------------------ Store data files to database---------------------
# StoreCustomer.store_all(customer_list, database_cursor, connection)
# StoreProduct.store_all(product_list, database_cursor, connection)
# StoresSalesOutlet.store_all(sales_outlet_list, database_cursor, connection)
# StoreSalesTarget.store_all(sales_target_list, database_cursor, connection)
