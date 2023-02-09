from datetime import datetime


def get_customers(cursor, number_customer):
    sql = "SELECT c.customer_first_name , c.customer_since " \
          "FROM customer " \
          "AS c "
    cursor.execute(sql)
    records = cursor.fetchall()
    customer_array = []
    if len(records) >= 1:
        for row in records:
            customer_name = row[0]
            customer_since = row[1]
            customer_array.append(Customer(customer_name, customer_since))

        customer_array.sort(key=lambda x: x.date)
        count = 0
        for customer in customer_array:
            if count == number_customer:
                break
            else:
                print("Customer Name : " + str(customer.name) + " Customer Since : " + str(customer.date.date()))
                count += 1
    else:
        print("There is not any customer yet")


class Customer:
    def __init__(self, name, date):
        self.name = name
        self.date = datetime.strptime(date, '%Y-%m-%d')
