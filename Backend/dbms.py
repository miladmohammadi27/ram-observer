import datetime
from contextlib import contextmanager
import sqlite3


class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance

class DBMSActions(metaclass=Singleton):

    def __init__(self, total_memory, used_memory, free_memory):
        self.total_memory = total_memory
        self.used_memory = used_memory
        self.free_memory = free_memory

    def write_ram_state(self):
        connection = self.connect_to_database()
        current_time = datetime.datetime.now()
        print(current_time)
        with connection as c:
            c.execute(f"""INSERT INTO API_ramstatus (total, used, free, report_date )
             VALUES ({self.total_memory}, {self.used_memory}, {self.free_memory}, datetime('now', 'localtime'));""")
            c.commit()

    @staticmethod
    @contextmanager
    def connect_to_database():
        connection = sqlite3.connect('../db.sqlite3')
        yield connection
        connection.close()

a = DBMSActions(10, 50, 45).write_ram_state()