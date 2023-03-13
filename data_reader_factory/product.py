import pandas as pd
from data_reader_factory import object_creator


class ProductDataReader:

    def __init__(self, path_file):
        self.path_file = path_file

    def read_data(self):
        data = pd.read_csv(self.path_file)
        product_list = []
        for index in data.index:
            product_id = data['product_id'][index]
            product_group = data['product_group'][index]
            product_type = data['product_type'][index]
            product = data['product'][index]
            price = data['current_retail_price'][index]
            product_obj = object_creator.create_product_obj(product_id,
                                                            product_group,
                                                            product_type,
                                                            product,
                                                            price)
            product_list.append(product_obj)

        return product_list
