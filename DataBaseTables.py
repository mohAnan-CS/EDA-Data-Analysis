def create_sales_target_table(cursor):
    cursor.execute('''create table sales_target(
                        sales_outlet_id int ,
                        year_month_date char(30), 
                        beans_goal int, 
                        beverage_goal int, 
                        food_goal int,  
                        merchandise_goal int,  
                        total_goal int,  
                        primary key (sales_outlet_id));
                    ''')


def create_customer_table(cursor):
    cursor.execute('''create table customer(
                        customer_id int ,
                        customer_first_name varchar(30), 
                        customer_since varchar(30), 
                        gender varchar(10),
                        birthdate varchar(20),
                        primary key(customer_id));
                    ''')


def create_transaction_table(cursor):
    cursor.execute('''create table transaction(
                        transaction_id int, 
                        instore_yn boolean, 
                        customer_id int, 
                        sales_outlet_id int,  
                        primary key (transaction_id),
                        FOREIGN KEY (sales_outlet_id) REFERENCES sales_target(sales_outlet_id),
                        FOREIGN KEY (customer_id) REFERENCES customer(customer_id));
                        ''')


def create_products_table(cursor):
    cursor.execute('''create table products(
                        product_id int ,
                        product_type varchar(30), 
                        product varchar(30),
                        current_retail_price float,
                        primary key (product_id));
                    ''')
