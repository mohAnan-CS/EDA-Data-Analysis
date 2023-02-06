def create_customer_obj(customer_id, customer_first_name, customer_since, birthdate, gender):
    customer_item = {
        "customer_id": customer_id,
        "customer_first_name": customer_first_name,
        "customer_since": customer_since,
        "birthdate": birthdate,
        "gender": gender,
    }
    return customer_item
