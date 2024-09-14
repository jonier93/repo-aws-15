import pymysql

host = "inst-db-15.crkkwims2ejn.us-east-2.rds.amazonaws.com"
user = "jonier"
passw = "12345678"
db_name = "db_users"

def connection_SQL():
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=passw,
            database=db_name
        )
        print("Succesfull connection to database")
        return connection
    except Exception as err:
        print("Error", err)
        return None

def insert(id, name, lastname, birthday):
    try:
        instruction = "INSERT INTO users VALUES ("+id+", '"+name+"', '"+lastname+"', '"+birthday+"');"
        connection = connection_SQL()
        cursor = connection.cursor()
        cursor.execute(instruction)
        connection.commit()
        print("User added")
    except Exception as err:
        print("Error", err)
        return None
