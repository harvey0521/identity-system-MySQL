import pyodbc


print(pyodbc.drivers())  # 查驅動名稱 'ODBC Driver 17 for SQL Server'

server = "172.16.45.213"
database = "TEST"  # 資料庫名稱：TEST
username = "sqlap"
password = "Ubot@1234"
driver = "ODBC Driver 17 for SQL Server"

print(f"SERVER={server};DATABASE={database};UID={username};PWD={password};DRIVER={{{driver}}}")

def get_db():
    return pyodbc.connect(
        f"SERVER={server};DATABASE={database};UID={username};PWD={password};DRIVER={{{driver}}}"
    )
