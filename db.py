import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def save_data(title,source,url,published_date,ai_summary):
    connection=psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host="localhost",
        port="5432"
    )
    cursor=connection.cursor()
    query= "INSERT INTO analayzed_articles(title,source,url,published_date,ai_summary) VALUES(%s,%s,%s,%s,%s)"

    data_t=(title,source,url,published_date,ai_summary)
    cursor.execute(query,data_t)

    connection.commit()
    cursor.close()
    connection.close()

    print("Successfully saved to database!")