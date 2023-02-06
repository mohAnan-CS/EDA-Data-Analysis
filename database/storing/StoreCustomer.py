def store_all(list_customer, cursor, mydb):
    for data in list_customer:
        cus_id = data['customer_id']
        customer_found = customer_is_found(str(cus_id), cursor)
        if not customer_found:
            store_customer(data['customer_id'], data['customer_first_name'], data['customer_since'], data['gender'], data['birthdate'], cursor, mydb)


def store_customer(customer_id, customer_first_name, customer_since, gender, birthdate, cursor, mydb):
    insert_customer_sql = "insert into customer (customer_id, customer_first_name, customer_since, gender, birthdate) values (%s, %s, %s, %s ,%s)"
    values = (str(customer_id), customer_first_name, customer_since, gender, birthdate)
    cursor.execute(insert_customer_sql, values)
    mydb.commit()


def customer_is_found(customer_id, cursor):
    check_customer_sql = "select * from customer where customer_id = " + customer_id + ";"
    cursor.execute(check_customer_sql)
    customer_records = cursor.fetchall()
    if len(customer_records) >= 1:
        return True
    else:
        return False
