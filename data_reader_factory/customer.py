import pandas as pd
from data_reader_factory import object_creator


def read_customer_file(path_file):
    data = pd.read_csv(path_file)
    customer_list = []
    for index in data.index:
        cus_id = data['customer_id'][index]
        cus_first_name = data['customer_first-name'][index]
        cus_since = data['customer_since'][index]
        cus_birthdate = data['birthdate'][index]
        cus_gender = data['gender'][index]
        customer_obj = ObjectCreator.create_customer_obj(cus_id,
                                                         cus_first_name,
                                                         cus_since,
                                                         cus_birthdate,
                                                         cus_gender, )

        customer_list.append(customer_obj)

    return customer_list
