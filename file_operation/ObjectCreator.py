def create_customer_obj(customer_id, customer_first_name, customer_since, birthdate, gender):
    customer_item = {
        "customer_id": customer_id,
        "customer_first_name": customer_first_name,
        "customer_since": customer_since,
        "birthdate": birthdate,
        "gender": gender,
    }
    return customer_item


def create_product_obj(product_id, product_type, product, current_retail_price):
    product_obj = {
        "product_id": product_id,
        "product_type": product_type,
        "product": product,
        "current_retail_price": current_retail_price,
    }
    return product_obj


def create_sales_outlet_obj(sales_outlet_id, sales_outlet_type, store_square_feet, store_address):
    sales_outlet_obj = {
        "sales_outlet_id": sales_outlet_id,
        "sales_outlet_type": sales_outlet_type,
        "store_square_feet": store_square_feet,
        "store_address": store_address,
    }
    return sales_outlet_obj


def create_sales_outlet_target_obj(sales_outlet_id, year_month_date, beans_goal, beverage_goal, food_goal, merchandise_goal, total_goal):
    sales_outlet_target = {
        "sales_outlet_id": sales_outlet_id,
        "year_month_date": year_month_date,
        "beans_goal": beans_goal,
        "beverage_goal": beverage_goal,
        "food_goal": food_goal,
        "merchandise_goal": merchandise_goal,
        "total_goal": total_goal,
    }
    return sales_outlet_target
