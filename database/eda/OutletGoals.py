def get_sales_goal(cursor, month_year, out_id):
    sql = "SELECT * " \
          "FROM sales_target"
    cursor.execute(sql)
    records = cursor.fetchall()
    outlet_goal_array = []
    if len(records) >= 1:

        for row in records:
            if out_id == row[0]:
                outlet_id = int(row[0])
                year_month = row[1]
                beans_goal = row[2]
                beverage_goal = row[3]
                food_goal = row[4]
                merchandise_goal = row[5]
                total_goal = row[6]
                goal_obj = create_sold_object(outlet_id, year_month, beans_goal, beverage_goal, food_goal,
                                              merchandise_goal,
                                              total_goal)
                outlet_goal_array.append(goal_obj)

        get_total_quantity_products(cursor, out_id, month_year, outlet_goal_array)
    else:
        print("There is no goals for any outlet")


def get_total_quantity_products(cursor, outlet_id, year_month, outlet_goal_array):
    sql = "SELECT t.transaction_id ,tp.quantity ,p.product_group ,td.transaction_date " \
          "FROM transaction " \
          "AS t " \
          "JOIN transaction_product " \
          "AS tp " \
          "ON t.transaction_id = tp.transaction_id " \
          "JOIN products " \
          "AS p " \
          "ON tp.product_id = p.product_id " \
          "JOIN transaction_details " \
          "AS td " \
          "ON t.transaction_id = td.transaction_id"
    cursor.execute(sql)
    records = cursor.fetchall()
    food, beverages, beans, merchandise = 0, 0, 0, 0
    if len(records) >= 1:
        for row in records:
            date = row[3]
            date_split = date.split("-")
            year = date_split[0]
            month = date_split[1]
            year_month_new = year + "-" + month
            if row[0] == outlet_id and year_month_new == year_month:
                quantity = row[1]
                if row[2].lower() == 'food':
                    food += quantity
                elif row[2].lower() == 'beverages':
                    beverages += quantity
                elif row[2].lower() == 'beans':
                    beans += quantity
                elif row[2].lower() == 'merchandise':
                    merchandise += quantity
        print_totals(outlet_id, year_month, outlet_goal_array, beans, beverages, food, merchandise)


def print_totals(outlet_id, year_month, outlet_goal_array, beans, beverages, food, merchandise):
    total_goal = 0
    for data in outlet_goal_array:
        if data["beans_goal"] <= beans:
            print("* Total beans for", year_month, "in outlet", outlet_id, "is", beans, ", Reach goal ...")
        elif data["beans_goal"] > beans:
            print("* Total beans for", year_month, "in outlet", outlet_id, "is", beans, ",Doesnt Reach goal ...")

        if data["beverage_goal"] <= beverages:
            print("* Total beverage for", year_month, "in outlet", outlet_id, "is", beverages, ",Reach goal ...")
        elif data["beans_goal"] > beverages:
            print("* Total beverage for ", year_month, "in outlet", outlet_id, "is", beverages, ",Doesnt Reach goal ...")

        if data["food_goal"] <= food:
            print("* Total food for", year_month, " in outlet", outlet_id, "is ", food, " ,Reach goal ...")
        elif data["food_goal"] > food:
            print("* Total food for", year_month, " in outlet", outlet_id, "is", food, " ,Doesnt Reach goal ...")

        if data["merchandise_goal"] <= merchandise:
            print("* Total merchandise for", year_month, "in outlet", outlet_id, "is", merchandise, " ,Reach goal ...")
        elif data["merchandise_goal"] > merchandise:
            print("* Total merchandise for", year_month, "in outlet", outlet_id, "is", merchandise, " ,Doesnt Reach goal ...")
        total_goal += data['total_goal']

    total = beans + beverages + food + merchandise
    if total_goal <= total:
        print("* Total is", total, "Reach total goal")
    else:
        print("* Total is", total, "Doesnt Reach total goal")


def create_sold_object(outlet_id, year_month, beans_goal, beverage_goal, food_goal, merchandise_goal, total_goal):
    goal_obj = {
        "outlet_id": outlet_id,
        "year_month": year_month,
        "beans_goal": beans_goal,
        "beverage_goal": beverage_goal,
        "food_goal": food_goal,
        "merchandise_goal": merchandise_goal,
        "total_goal": total_goal,
    }
    return goal_obj
