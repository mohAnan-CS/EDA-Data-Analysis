def create_database(cursor, database_name):
    cursor.execute("CREATE DATABASE " + database_name + ";")
    cursor.execute("USE " + database_name + ";")
