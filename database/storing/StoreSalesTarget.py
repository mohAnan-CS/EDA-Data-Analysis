def store_all(list_sales_target, cursor, mydb):
    for data in list_sales_target:
        sales_outlet_id = data['sales_outlet_id']
        sales_outlet_found = sales_target_is_found(str(sales_outlet_id), cursor)
        if sales_outlet_found:
            store_sales_target(data['sales_outlet_id'], data['year_month'], data['beans_goal'], data['beverage_goal'], data['food_goal'], data['merchandise_goal'], data['total_goal'], cursor, mydb)


def store_sales_target(sales_outlet_id, year_month_date, beans_goal, beverage_goal, food_goal, merchandise_goal, total_goal, cursor, mydb):
    insert_sales_target_sql = "INSERT INTO sales_target (sales_outlet_id, year_month_date, beans_goal, beverage_goal, food_goal, merchandise_goal, total_goal) " \
                              "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (str(sales_outlet_id), year_month_date, str(beans_goal), str(beverage_goal), str(food_goal), str(merchandise_goal), str(total_goal))
    cursor.execute(insert_sales_target_sql, values)
    mydb.commit()


def sales_target_is_found(sales_outlet_id, cursor):
    check_sales_outlet_sql = "SELECT * " \
                             "FROM sales_outlet " \
                             "WHERE sales_outlet_id = " + sales_outlet_id + ";"
    cursor.execute(check_sales_outlet_sql)
    sales_target_records = cursor.fetchall()
    if len(sales_target_records) >= 1:
        return True
    else:
        return False
