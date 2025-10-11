import sqlite3

class Connect:
    def __init__(self, db_name="api.db"):
        self.db_name = db_name
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def init_db(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
    
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                year INTEGER,
                city TEXT
            )
        """)
    
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                value TEXT NOT NULL,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES Usuario(id)
            )
        """)
        conn.commit()
        conn.close()
