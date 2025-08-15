import mysql.connector


def get_db():
    conn = mysql.connector.connect(
        host="localhost",  # 主機位置，如果你用本地的 MySQL 就是 localhost
        user="root",  # 你的 MySQL 帳號
        password="12345173988475",  # 你的 MySQL 密碼
        database="work-training",  # 你的資料庫名稱
        charset="utf8mb4",  # 避免中文亂碼
    )
    return conn
