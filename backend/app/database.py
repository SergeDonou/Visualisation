import os
import psycopg2
from dotenv import load_dotenv

# Charger le fichier .env
load_dotenv()

def get_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        print("Connexion PostgreSQL réussie.")
        return conn
    except Exception as e:
        print("Erreur de connexion à PostgreSQL :", e)
        return None


def test_connection():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()
        print("Résultat du test SELECT 1 :", result)
        cursor.close()
        conn.close()


if __name__ == "__main__":
    test_connection()
