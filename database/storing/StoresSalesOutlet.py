def store_all(list_sales_outlet, cursor, mydb):
    for data in list_sales_outlet:
        sales_outlet_id = data['sales_outlet_id']
        sales_outlet_found = sales_outlet_is_found(str(sales_outlet_id), cursor)
        if not sales_outlet_found:
            store_sales_outlet(data['sales_outlet_id'], data['sales_outlet_type'], data['store_square_feet'], data['store_address'], cursor, mydb)


def store_sales_outlet(sales_outlet_id, sales_outlet_type, store_square_feet, store_address, cursor, mydb):
    insert_sales_outlet_sql = "INSERT INTO sales_outlet (sales_outlet_id, sales_outlet_type, store_square_feet, store_address) " \
                              "VALUES (%s, %s, %s, %s)"
    values = (str(sales_outlet_id), sales_outlet_type, str(store_square_feet), store_address)
    cursor.execute(insert_sales_outlet_sql, values)
    mydb.commit()


def sales_outlet_is_found(sales_outlet_id, cursor):
    check_sales_outlet_sql = "SELECT * " \
                             "FROM sales_outlet " \
                             "WHERE sales_outlet_id = " + sales_outlet_id + ";"
    cursor.execute(check_sales_outlet_sql)
    sales_outlet_records = cursor.fetchall()
    if len(sales_outlet_records) >= 1:
        return True
    else:
        return False
