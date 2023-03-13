from data_reader_factory.reader_factory import DataReader
from database_factory import connector
from data_analysis_factory import demand_outlet, first_customers, gender_popular, outlet_goals, sales_time, \
    sold_products

connection = connector.connect("root", "localhost", "0000")
database_cursor = connection.cursor()
# database_cursor.execute("DROP DATABASE SalesDataBase;")
# DataBaseCreator.create_database(database_cursor, "SalesDataBase")
database_cursor.execute("USE SalesDataBase")
# DataBaseTables.create_tables(database_cursor)

customer_path = "C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\customer.csv"
product_path = "C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\product.csv"
sales_outlet_path = "C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\sales_outlet.csv"
sales_target_path = "C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\sales_targets.csv"
transaction_path = "C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\201904 sales reciepts.csv"

# ----------------- Read data files ----------------------
# Create CustomerDataReaderFactory object
data_reader_factory = DataReader()

# Create CustomerDataReader object
customer_data_reader = data_reader_factory.create_reader(customer_path)

# Read customer data
customer_list = customer_data_reader.read_data()

#################

# Create ProductDataReader object
product_data_reader = data_reader_factory.create_reader(product_path)

# Read product data
product_list = product_data_reader.read_data()

###############

sales_outlet_reader = data_reader_factory.create_reader(sales_outlet_path)
sales_outlet = sales_outlet_reader.read_data()


############

sales_target_reader = data_reader_factory.create_reader(sales_target_path)
sales_target = sales_target_reader.read_data()

#########

transaction_reader = data_reader_factory.create_reader(transaction_path)
transaction = transaction_reader.read_data()
print(transaction)

# product_list = ReadProduct.read_product_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\product.csv")
# sales_outlet_list = ReadSalesOutlet.read_sales_outlet_file(
#     "C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\sales_outlet.csv")
# sales_target_list = ReadSalesTarget.read_sales_target_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\sales_targets.csv")
# transaction_list = ReadTransaction.read_transaction_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\201904 sales reciepts.csv")
# ---------------------------------------------------------

# ------------------ Store data files to database_factory---------------------
# StoreCustomer.store_all(customer_list, database_cursor, connection)
# StoreProduct.store_all(product_list, database_cursor, connection)
# StoresSalesOutlet.store_all(sales_outlet_list, database_cursor, connection)
# StoreSalesTarget.store_all(sales_target_list, database_cursor, connection)
# StoreTransaction.store_all(transaction_list, database_cursor, connection)
# ----------------------------------------------------------

# ------------------ EDA Questions ---------------------

# -  What are the most sold items?
# -  What are the least sold items?
# print()
# print("------------------------ EDA Questions with their answers ------------------------")
# print()
# print("- What are the most 5 sold items ?")
# print()
# sold_products.get_sold_products_sorted(database_cursor, True)
# print()
# print("- What are the less 5 sold items ?")
# print()
# sold_products.get_sold_products_sorted(database_cursor, False)
# print()
# print("-----------------------------------------------------------------------------------------------------------")
# print()
#
# # - Which is the best times for selling in store ?
# # - which is the worst times for selling in store ?
# print("- Which is the best time for selling in store ?")
# print()
# sales_time.get_time(True, database_cursor)
# print()
# print("- Which is the worst time for selling in store ?")
# print()
# sales_time.get_time(False, database_cursor)
# print()
# print("-----------------------------------------------------------------------------------------------------------")
# print()
# # - Is there a lot of demand outside the restaurant ?
# print("- Is there a lot of demand outside the store 3 ?")
# print()
# demand_outlet.get_transaction_in_out(database_cursor, 3)
# print()
# print("-----------------------------------------------------------------------------------------------------------")
# print()
# # -  Are males more popular or females in certain outlet?
# print("- Are males more popular or females in 3 outlet")
# print()
# gender_popular.get_male_female(database_cursor, 3)
# print()
# print("-----------------------------------------------------------------------------------------------------------")
# print()
# # - what is the first customers since outlet opened ?
# print("- What is the first five customer sice outlet opened ?")
# print()
# first_customers.get_customers(database_cursor, 4)
# print()
# print("-----------------------------------------------------------------------------------------------------------")
# print()
# # - is beans goal reach for last month ?
# # - is beverage goal reach for last month ?
# # - is merchandise goal reach for last month ?
# # is reach total goal ?
# print("- Is beans, beverage, merchandise, total goal are reach in -> 2019-04 ?")
# print()
# outlet_goals.get_sales_goal(database_cursor, "2019-04", 4)
# print()
# print("-----------------------------------------------------------------------------------------------------------")
