from database.storing import StoreCustomer, StoresSalesOutlet


def store_all(list_transaction, cursor, mydb):
    for data in list_transaction:
        transaction_id = data['transaction_id']
        customer_id = data['customer_id']
        sales_outlet_id = data['sales_outlet_id']

        customer_found = StoreCustomer.customer_is_found(str(customer_id), cursor)
        sales_outlet_found = StoresSalesOutlet.sales_outlet_is_found(str(sales_outlet_id), cursor)
        transaction_found = transaction_is_found(transaction_id, cursor)

        if customer_found and sales_outlet_found:
            if not transaction_found:
                store_transaction(data['transaction_id'], data['instore_yn'], data['customer_id'], data['sales_outlet_id'], cursor, mydb)
                store_transaction_details(data['transaction_id'], data['transaction_date'], data['transaction_time'], cursor, mydb)
            else:
                store_transaction_product(data['transaction_id'], data['quantity'], data['line_item_amount'], data['product_id'], cursor, mydb)


def store_transaction(transaction_id, instore_yn, customer_id, sales_outlet_id, cursor, mydb):
    in_store = True
    if instore_yn == 'Y':
        in_store = True
    elif instore_yn == 'N':
        in_store = False

    insert_transaction_sql = "INSERT INTO transaction (transaction_id, instore_yn, customer_id, sales_outlet_id) " \
                             "VALUES (%s, %s, %s, %s)"
    values = (str(transaction_id), in_store, str(customer_id), str(sales_outlet_id))

    cursor.execute(insert_transaction_sql, values)
    mydb.commit()


def store_transaction_product(transaction_id, quantity, line_item_amount, product_id, cursor, mydb):
    insert_transaction_product_sql = "INSERT INTO transaction_product (transaction_id, quantity, line_item_amount, product_id) " \
                                     "VALUES (%s, %s, %s, %s)"
    values = (str(transaction_id), str(quantity), str(line_item_amount), str(product_id))
    cursor.execute(insert_transaction_product_sql, values)
    mydb.commit()


def store_transaction_details(transaction_id, transaction_date, transaction_time, cursor, mydb):
    insert_transaction_details_sql = "INSERT INTO transaction_details (transaction_id, transaction_date, transaction_time) " \
                                     "VALUES (%s, %s, %s)"
    values = (str(transaction_id), transaction_date, transaction_time)
    cursor.execute(insert_transaction_details_sql, values)
    mydb.commit()


def transaction_is_found(transaction_id, cursor):
    check_transaction_sql = "SELECT * FROM transaction WHERE transaction_id = " + str(transaction_id) + ";"
    cursor.execute(check_transaction_sql)
    transaction_records = cursor.fetchall()
    if len(transaction_records) >= 1:
        return True
    else:
        return False
