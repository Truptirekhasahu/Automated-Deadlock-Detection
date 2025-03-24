import sqlite3

class DeadlockLogger:
    def __init__(self, db_name="deadlock_log.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, processes TEXT)''')
        self.conn.commit()

    def log_deadlock(self, processes):
        self.cursor.execute("INSERT INTO logs (processes) VALUES (?)", (",".join(processes),))
        self.conn.commit()
