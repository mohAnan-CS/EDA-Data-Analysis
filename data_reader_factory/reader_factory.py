from data_reader_factory.customer import CustomerDataReader
from data_reader_factory.product import ProductDataReader
from data_reader_factory.sales_outlet import SalesOutletDataReader
from data_reader_factory.sales_target import SalesTargetDataReader
from data_reader_factory.transaction import TransactionDataReader


class DataReaderFactory:
    def create_reader(self, path_file):
        pass


# Concrete Factory Class
class DataReader(DataReaderFactory):
    def create_reader(self, path_file):

        file_name_split = path_file.split("\\")
        last_index = len(file_name_split)
        file_name = file_name_split[last_index-1]

        if file_name == "customer.csv":
            return CustomerDataReader(path_file)
        elif file_name == "product.csv":
            return ProductDataReader(path_file)
        elif file_name == "sales_outlet.csv":
            return SalesOutletDataReader(path_file)
        elif file_name == "sales_targets.csv":
            return SalesTargetDataReader(path_file)
        elif file_name == "201904 sales reciepts.csv":
            return TransactionDataReader(path_file)
