def get_goals(cursor, month_year, out_id):
    sql = "SELECT * " \
          "FROM sales_target"
    cursor.execute(sql)
    records = cursor.fetchall()
    outlet_goal_array = []
    if len(records) >= 1:
        for row in records:
            if month_year == row[1] and out_id == row[0]:
                outlet_id = int(row[0])
                year_month = row[1]
                beans_goal = row[2]
                beverage_goal = row[3]
                food_goal = row[4]
                merchandise_goal = row[5]
                total_goal = row[6]
                goal_obj = create_sold_object(outlet_id, year_month, beans_goal, beverage_goal, food_goal, merchandise_goal,
                                              total_goal)
                outlet_goal_array.append(goal_obj)

        print(outlet_goal_array)
        return outlet_goal_array
    else:
        print("There is no goals for any outlet")
        return outlet_goal_array


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
