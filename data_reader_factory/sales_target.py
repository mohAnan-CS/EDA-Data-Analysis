import pandas as pd
from data_reader_factory import object_creator


class SalesTargetDataReader:

    def __init__(self, path_file):
        self.path_file = path_file

    def read_data(self):
        data = pd.read_csv(self.path_file)
        sales_outlet_target_list = []
        for index in data.index:
            sales_outlet_id = data['sales_outlet_id'][index]
            year_month_date = data['year_month'][index]
            beans_goal = data['beans_goal'][index]
            beverage_goal = data['beverage_goal'][index]
            food_goal = data['food_goal'][index]
            merchandise_goal = data['merchandise _goal'][index]
            total_goal = data['total_goal'][index]
            sales_outlet_target_obj = object_creator.create_sales_target_obj(sales_outlet_id,
                                                                             year_month_date,
                                                                             beans_goal,
                                                                             beverage_goal,
                                                                             food_goal,
                                                                             merchandise_goal,
                                                                             total_goal)
            sales_outlet_target_list.append(sales_outlet_target_obj)

        return sales_outlet_target_list
