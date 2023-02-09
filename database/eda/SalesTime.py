def get_sales_time(cursor):
    sql = "SELECT t.transaction_id , t.transaction_time " \
          "FROM transaction_details " \
          "AS t"
    cursor.execute(sql)
    records = cursor.fetchall()
    sales_time_array = []
    if len(records) >= 1:
        for row in records:
            transaction_id = row[0]
            transaction_time = row[1]
            sales_time_obj = create_sales_time_object(transaction_id, transaction_time)
            sales_time_array.append(sales_time_obj)

    print_times(False, sales_time_array)


def print_times(is_time_best, sales_time_array):

    # six_nine, nine_twelve, twelve_fifteen, fifteen_eighteen, eighteen_twenty_one, twenty_one_twenty_four = 0, 0, 0, 0, 0, 0
    array_hours = [0, 0, 0, 0, 0, 0]
    for sale in sales_time_array:
        time = sale['transaction_time'].split(":")
        hour = int(time[0])
        if (hour >= 6) and (hour < 9):
            array_hours[0] += 1
        elif (hour >= 9) and (hour < 12):
            array_hours[1] += 1
        elif (hour >= 12) and (hour < 15):
            array_hours[2] += 1
        elif (hour >= 15) and (hour < 18):
            array_hours[3] += 1
        elif (hour >= 18) and (hour < 21):
            array_hours[4] += 1
        elif (hour >= 21) and (hour < 24):
            array_hours[5] += 1

    if is_time_best:
        best_time = max(array_hours)
        index_best_time = array_hours.index(best_time)
        if index_best_time == 0:
            print("The best time for selling is from 6:00 - 9:00")
        elif index_best_time == 1:
            print("The best time for selling is from 9:00 - 12:00")
        elif index_best_time == 2:
            print("The best time for selling is from 12:00 - 15:00")
        elif index_best_time == 3:
            print("The best time for selling is from 15:00 - 18:00")
        elif index_best_time == 4:
            print("The best time for selling is from 18:00 - 21:00")
        else:
            print("The best time for selling is from 21:00 - 24:00")
    else:
        worst_time = min(array_hours)
        index_worst_time = array_hours.index(worst_time)
        if index_worst_time == 0:
            print("The worst time for selling is from 6:00 - 9:00")
        elif index_worst_time == 1:
            print("The worst time for selling is from 9:00 - 12:00")
        elif index_worst_time == 2:
            print("The worst time for selling is from 12:00 - 15:00")
        elif index_worst_time == 3:
            print("The worst time for selling is from 15:00 - 18:00")
        elif index_worst_time == 4:
            print("The worst time for selling is from 18:00 - 21:00")
        else:
            print("The worst time for selling is from 21:00 - 24:00")


def create_sales_time_object(transaction_id, transaction_time):
    sales_time_obj = {
        "transaction_id": transaction_id,
        "transaction_time": transaction_time,
    }
    return sales_time_obj
