import os
import pymysql
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def get_demo_data():
    """demo_tableの全レコードを取得してJSON返却"""
    connection = pymysql.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        port=int(os.environ.get('DB_PORT', 3306)),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', ''),
        database=os.environ.get('DB_NAME', 'demo_database'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
  
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM demo_table")
            data = cursor.fetchall()
            return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
