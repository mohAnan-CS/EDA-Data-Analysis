def get_male_female(cursor, sales_outlet_id):
    sql = "SELECT * " \
          "FROM transaction " \
          "AS t " \
          "JOIN customer " \
          "AS c " \
          "ON t.customer_id = c.customer_id " \
          "WHERE t.sales_outlet_id = " + str(sales_outlet_id)
    cursor.execute(sql)
    records = cursor.fetchall()
    female, male = 0, 0
    if len(records) >= 1:
        for row in records:
            gender = row[7].strip()
            if gender == "M":
                male += 1
            elif gender == "F":
                female += 1

        print("Number of male customer in outlet " + str(sales_outlet_id) + " : " + str(male))
        print("Number of female customer in outlets :" + str(sales_outlet_id) + " : " + str(female))
    else:
        print("Outlet " + str(sales_outlet_id) + " not found or There is not any customer yet")
