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
