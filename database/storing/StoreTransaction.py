from database.storing import StoreCustomer, StoresSalesOutlet


def store_all(list_transaction, cursor, mydb):
    for data in list_transaction:
        customer_id = data['customer_id']
        sales_outlet_id = data['sales_outlet_id']
        customer_found = StoreCustomer.customer_is_found(str(customer_id), cursor)
        sales_outlet_found = StoresSalesOutlet.sales_outlet_is_found(str(sales_outlet_id), cursor)
        if customer_found and sales_outlet_found:
            store_transaction(data['transaction_id'], data['instore_yn'], data['customer_id'], data['sales_outlet_id'], cursor, mydb)


def store_transaction(transaction_id, instore_yn, customer_id, sales_outlet_id, cursor, mydb):
    insert_transaction_sql = "insert into transaction (transaction_id, instore_yn, customer_id, sales_outlet_id) VALUES (%s, %s, %s, %s)"
    values = (str(transaction_id), str(instore_yn), str(customer_id), str(sales_outlet_id))
    cursor.execute(insert_transaction_sql, values)
    mydb.commit()


