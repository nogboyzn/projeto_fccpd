from flask import Flask, jsonify
import redis
import psycopg2
import os
import time

app = Flask(__name__)

# Environment Configuration
REDIS_HOST = os.environ.get('REDIS_HOST', 'session_store')
DB_HOST = os.environ.get('DB_HOST', 'user_db')
DB_NAME = os.environ.get('DB_NAME', 'users_db')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASS = os.environ.get('DB_PASS', 'password')

# Connect to Redis (Session Store)
# Retry logic for robustness
def get_redis_connection():
    return redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

# Connect to Postgres (User DB)
def get_db_connection():
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
    return conn

@app.route('/')
def dashboard():
    # Interaction with Session Store (Redis)
    try:
        cache = get_redis_connection()
        visits = cache.incr('portal_hits')
    except Exception as e:
        visits = f"Redis Error: {str(e)}"

    # Interaction with User DB (Postgres)
    db_status = "Unchecked"
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()[0]
        cur.close()
        conn.close()
        db_status = f"Connected: {db_version}"
    except Exception as e:
        db_status = f"Postgres Error: {str(e)}"

    return jsonify({
        "component": "portal_app_v1",
        "session_store_stats": {
            "total_visits": visits,
            "engine": "Redis"
        },
        "user_db_health": {
            "status": db_status,
            "engine": "PostgreSQL"
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
