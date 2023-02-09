from database import Connector
from file_reader import ReadCustomer, ReadProduct, ReadSalesOutlet, ReadSalesTarget, ReadTransaction
from database.storing import StoreCustomer, StoreProduct, StoresSalesOutlet, StoreSalesTarget, StoreTransaction
from database.eda import SoldProducts, SalesTime, DemandInOutOutlet, MaleFemalePopular, FirstCustomers, OutletGoals

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
#     "C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\sales_outlet.csv")
# sales_target_list = ReadSalesTarget.read_sales_target_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\sales targets.csv")
# transaction_list = ReadTransaction.read_transaction_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\201904 sales reciepts.csv")
# ---------------------------------------------------------

# ------------------ Store data files to database---------------------
# StoreCustomer.store_all(customer_list, database_cursor, connection)
# StoreProduct.store_all(product_list, database_cursor, connection)
# StoresSalesOutlet.store_all(sales_outlet_list, database_cursor, connection)
# StoreSalesTarget.store_all(sales_target_list, database_cursor, connection)
# StoreTransaction.store_all(transaction_list, database_cursor, connection)
# ----------------------------------------------------------

# ------------------ EDA Questions ---------------------

# -  What are the most sold items?
# -  What are the least sold items?
# SoldProducts.get_sold_products_sorted(database_cursor, False)

# - Which is the best times for selling in store ?
# - which is the worst times for selling in store ?
# SalesTime.get_time(False, database_cursor)

# - Is there a lot of demand outside the restaurant ?
# DemandInOutOutlet.get_transaction_in_out(database_cursor, 3)

# -  Are males more popular or females in certain outlet?
# MaleFemalePopular.get_male_female(database_cursor, 3)

# - what is the first customers since outlet opened ?
# FirstCustomers.get_customers(database_cursor, 4)

# - is beans goal reach for last month ?
# - is beverage goal reach for last month ?
# - is merchandise goal reach for last month ?
OutletGoals.get_goals(database_cursor, "Apr-19", 3)
