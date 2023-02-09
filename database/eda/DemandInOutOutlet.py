def get_transaction_in_out(cursor):
    sql = "SELECT t.transaction_id , t.instore_yn " \
          "FROM transaction " \
          "AS t"
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

    print("Number of transaction inside the outlet :" + str(inside))
    print("Number of transaction outside the outlet :" + str(outside))
