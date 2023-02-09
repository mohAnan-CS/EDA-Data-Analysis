def get_transaction_in_out(cursor, sales_outlet_id):
    sql = "SELECT t.transaction_id , t.instore_yn " \
          "FROM transaction " \
          "AS t " \
          "WHERE t.sales_outlet_id = " + str(sales_outlet_id)
    cursor.execute(sql)
    records = cursor.fetchall()
    outside, inside = 0, 0
    if len(records) >= 1:
        for row in records:
            instor_yn = row[1]
            if instor_yn == 1:
                inside += 1
            else:
                outside += 1

    print("* Number of transaction inside outlet " + str(sales_outlet_id) + " : " + str(inside))
    print("* Number of transaction outside outlet  " + str(sales_outlet_id) + " : " + str(outside))
    if inside > outside:
        print("Inside is more demand than outside ...")
    elif inside < outside:
        print("Outside is more demand than inside ...")
    else:
        print("Inside and outside are equal demand ...")
