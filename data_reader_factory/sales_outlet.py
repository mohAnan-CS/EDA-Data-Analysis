import pandas as pd
from data_reader_factory import object_creator


class SalesOutletDataReader:

    def __init__(self, path_file):
        self.path_file = path_file

    def read_data(self):
        data = pd.read_csv(self.path_file)
        sales_outlet_list = []
        for index in data.index:
            sales_outlet_id = data['sales_outlet_id'][index]
            sales_outlet_type = data['sales_outlet_type'][index]
            store_square_feet = data['store_square_feet'][index]
            store_address = data['store_address'][index]
            sales_outlet_obj = object_creator.create_sales_outlet_obj(sales_outlet_id,
                                                                      sales_outlet_type,
                                                                      store_square_feet,
                                                                      store_address)
            sales_outlet_list.append(sales_outlet_obj)

        return sales_outlet_list
