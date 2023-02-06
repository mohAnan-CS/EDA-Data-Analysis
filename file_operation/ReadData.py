import pandas as pd
from file_operation import ObjectCreator


def read_customer_file(path_file):
    data = pd.read_csv(path_file)
    customer_list = []
    for index in data.index:
        cus_id = data['customer_id'][index]
        cus_first_name = data['customer_first-name'][index]
        cus_since = data['customer_since'][index]
        cus_gender = data['gender'][index]
        cus_birthdate = data['birthdate'][index]
        customer_obj = ObjectCreator.create_customer_obj(cus_id,
                                                         cus_first_name,
                                                         cus_since,
                                                         cus_gender,
                                                         cus_birthdate)
        customer_list.append(customer_obj)

    return customer_list


def read_product_file(path_file):
    data = pd.read_csv(path_file)
    product_list = []
    for index in data.index:
        product_id = data['product_id'][index]
        product_type = data['product_type'][index]
        product = data['product'][index]
        price = data['current_retail_price'][index]
        product_obj = ObjectCreator.create_product_obj(product_id,
                                                       product_type,
                                                       product,
                                                       price)
        product_list.append(product_obj)

    return product_list


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


def read_sales_target_file(path_file):
    data = pd.read_csv(path_file)
    sales_outlet_target_list = []
    for index in data.index:
        sales_outlet_id = data['sales_outlet_id'][index]
        year_month_date = data['year_month'][index]
        beans_goal = data['beans_goal'][index]
        beverage_goal = data['beverage_goal'][index]
        food_goal = data['food_goal'][index]
        merchandise_goal = data['merchandise _goal'][index]
        total_goal = data['total_goal'][index]
        sales_outlet_target_obj = ObjectCreator.create_sales_target_obj(sales_outlet_id,
                                                                        year_month_date,
                                                                        beans_goal,
                                                                        beverage_goal,
                                                                        food_goal,
                                                                        merchandise_goal,
                                                                        total_goal)
        sales_outlet_target_list.append(sales_outlet_target_obj)

    for data in sales_outlet_target_list:
        print(data)
        print("\n")
