from psutil import virtual_memory
import bitmath
from Backend.dbms import DBMSActions

test = virtual_memory().total

result = bitmath.Byte(bytes=test).MB
print(type(result.value))
print(result.value)

# conn = sqlite3.connect('../db.sqlite3')

# sql = conn.execute("SELECT * From API_ramstatus")

# for q in sql:
#     print(q)
