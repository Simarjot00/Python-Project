import pymysql

# Create a connection to the database
try:
    conn = pymysql.connect(
        host="localhost",
        port=3307,
        user="root",
        password="",
        database="realestate"
    )
    mycur = conn.cursor()
    print("Connected to the database")
except pymysql.MySQLError as e:
    print(f"Error: {e}")
    conn = None

def alterations(query):
    mycur.execute(query)
    conn.commit()
def info(query):
    mycur.execute(query)
    return mycur
