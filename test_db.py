from database import get_db_connection

db = get_db_connection()

print("Database Connected Successfully!")

db.close()