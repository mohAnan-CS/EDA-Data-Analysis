import pandas as pd
from data_reader_factory import object_creator


def read_sales_outlet_file(path_file):
    data = pd.read_csv(path_file)
    sales_outlet_list = []
    for index in data.index:
        sales_outlet_id = data['sales_outlet_id'][index]
        sales_outlet_type = data['sales_outlet_type'][index]
        store_square_feet = data['store_square_feet'][index]
        store_address = data['store_address'][index]
        sales_outlet_obj = ObjectCreator.create_sales_outlet_obj(sales_outlet_id,
                                                                 sales_outlet_type,
                                                                 store_square_feet,
                                                                 store_address)
        sales_outlet_list.append(sales_outlet_obj)

    return sales_outlet_list
