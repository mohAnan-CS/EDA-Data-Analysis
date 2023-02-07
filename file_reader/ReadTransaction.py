import pandas as pd
from file_reader import ObjectCreator


def read_transaction_file(path_file):
    data = pd.read_csv(path_file)
    transaction_list = []
    for index in data.index:
        transaction_id = data['transaction_id'][index]
        instore_yn = data['instore_yn'][index]
        customer_id = data['customer_id'][index]
        sales_outlet_id = data['sales_outlet_id'][index]
        transaction_date = data['transaction_date'][index]
        transaction_time = data['transaction_time'][index]
        quantity = data['quantity'][index]
        line_item_amount = data['line_item_amount'][index]
        product_id = data['product_id'][index]

        transaction_obj = ObjectCreator.create_transaction_obj(transaction_id,
                                                               instore_yn,
                                                               customer_id,
                                                               sales_outlet_id,
                                                               transaction_date,
                                                               transaction_time,
                                                               quantity,
                                                               line_item_amount,
                                                               product_id
                                                               )
        transaction_list.append(transaction_obj)

    return transaction_list
