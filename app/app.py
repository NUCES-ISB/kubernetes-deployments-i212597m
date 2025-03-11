from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Database connection
DB_HOST = "postgres"
DB_NAME = os.getenv("POSTGRES_DB", "flaskdb")
DB_USER = os.getenv("POSTGRES_USER", "flaskuser")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "postgrespass")

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
        return "Connected to PostgreSQL!", 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
