def store_all(list_product, cursor, mydb):
    for data in list_product:
        product_id = data['product_id']
        product_found = product_is_found(str(product_id), cursor)
        if not product_found:
            store_product(data['product_id'], data['product_type'], data['product'], data['current_retail_price'], cursor, mydb)


def store_product(product_id, product_type, product, current_retail_price, cursor, mydb):
    insert_product_sql = "INSERT INTO products (product_id, product_type, product, current_retail_price) " \
                         "VALUES (%s, %s, %s, %s)"
    price = float(current_retail_price.replace("$", ""))
    values = (str(product_id), product_type, product, price)
    cursor.execute(insert_product_sql, values)
    mydb.commit()


def product_is_found(product_id, cursor):
    check_product_sql = "SELECT * " \
                        "FROM products " \
                        "WHERE product_id = " + product_id + ";"
    cursor.execute(check_product_sql)
    product_records = cursor.fetchall()
    if len(product_records) >= 1:
        return True
    else:
        return False
