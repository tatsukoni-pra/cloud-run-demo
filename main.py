import os
import requests
from flask import Flask, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, Session

app = Flask(__name__)

# PublicIP接続方式: データベース接続設定
def setup_database():
    """Unix ソケットでデータベースエンジンを設定"""
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_name = os.environ.get('DB_NAME')
    cloud_sql_connection_name = os.environ.get('INSTANCE_UNIX_SOCKET')
    engine_url = (
        f"mysql+pymysql://{db_user}:{db_pass}@/{db_name}?unix_socket={cloud_sql_connection_name}"
    )
    engine = create_engine(engine_url)
    
    return engine

# データベースエンジンとセッション設定
engine = setup_database()
session = scoped_session(sessionmaker(engine))

Base = declarative_base()
Base.query = session.query_property()

def yield_session():
    session = scoped_session(sessionmaker(engine))
    return session

def get_session():
    session = Session(engine)
    return session

@app.route("/")
def get_demo_data():
    """demo_tableの全レコードを取得してJSON返却"""
    db_session = get_session()
    
    try:
        result = db_session.execute(text("SELECT * FROM demo_table"))
        data = [dict(row._mapping) for row in result]
        return jsonify(data)
    finally:
        db_session.close()

@app.route("/ip-check")
def ip_check():
    url = 'https://inet-ip.info/ip'
    res = requests.get(url)
    return res.text

@app.route("/hello")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
