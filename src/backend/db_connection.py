import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

 # Load .env file
load_dotenv()

def get_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
    return conn

def get_all_qcbatches():
  
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT qcbatch_id FROM qcbatch ORDER BY qcbatch_id;")
            rows = cur.fetchall()
            return [row["qcbatch_id"] for row in rows] # Frontend recives clean value
    finally:
        conn.close()


def get_create_dt(qcbatch: str):
  
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT create_dt FROM qcbatch WHERE qcbatch_id = %s;", (qcbatch,))
            row = cur.fetchone()
            return row["create_dt"] if row else None
    finally:
        conn.close()


def get_analyses_for_batch(qcbatch: str):
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                SELECT 
                    a.analysis_type AS type,
                    a.analysis_status AS status
                FROM analysis a
                JOIN qcbatch q ON a.qcbatch_id = q.id
                WHERE q.qcbatch_id = %s;
                """,
                (qcbatch,),
            )
            return cur.fetchall()
    finally:
        conn.close()