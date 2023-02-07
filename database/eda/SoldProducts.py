def get_sold_products(cursor):
    sql = "SELECT transaction_product.transaction_id , " \
          "products.product_id, " \
          "products.product_type , " \
          "products. product , " \
          "transaction_product.quantity " \
          "FROM transaction_product " \
          "LEFT JOIN products " \
          "ON transaction_product.product_id = products.product_id;"
    cursor.execute(sql)
    records = cursor.fetchall()
    products_hashmap = {}
    if len(records) >= 1:
        for row in records:
            products_hashmap[row[0]] = create_sold_object(str(row[0]), str(row[1]), str(row[2]), str(row[3]),
                                                          str(row[4]))


def get_top_sold_products(products_hashmap):
    product_quantities = {}
    for entry in products_hashmap.values():
        product_id = entry["product_id"]
        product_type = entry["product_type"]
        product = entry["product"]
        quantity = int(entry["quantity"])
        if product_id in product_quantities:
            product_quantities[product_id]["quantity"] += quantity
        else:
            product_quantities[product_id] = {
                "product_id": product_id,
                "product_type": product_type,
                "product": product,
                "quantity": quantity
            }
    print(type(sorted(product_quantities.items(), key=lambda x: x[1]['quantity'], reverse=True)))


def create_sold_object(transaction_id, product_id, product_type, product, quantity):
    sold_obj = {
        "transaction_id": transaction_id,
        "product_id": product_id,
        "product_type": product_type,
        "product": product,
        "quantity": quantity,
    }
    return sold_obj
