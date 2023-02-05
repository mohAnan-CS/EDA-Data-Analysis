import pandas as pd


def create_customer_item(customer_id, customer_first_name, customer_since, birthdate, gender):
    customer_item = {
        "customer_id": customer_id,
        "customer_first_name": customer_first_name,
        "customer_since": customer_since,
        "birthdate": birthdate,
        "gender": gender,
    }
    return customer_item


def read_files(path_file):
    data_list = []
    data = pd.read_csv(path_file)
    data_list.append(data.values.tolist())
    return data_list
