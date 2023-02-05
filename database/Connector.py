import mysql.connector


def connect(db_username, db_host, db_password):
    mydb = mysql.connector.connect(
        host=db_host,
        user=db_username,
        password=db_password
    )
    return mydb
