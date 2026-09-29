import sqlite3

def setup_db():
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            source TEXT,
            url TEXT,
            date_pub TEXT
        )





    """)




    conn.commit()
    conn.close()

def save_article(article_list):
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()

    for article in article_list:
        cursor.execute("""
        INSERT INTO articles(title,source,url,date_pub)
        VALUES(?,?,?,?)
        
        
        """,(article.title,article.source,article.url,article.date_pub))
    conn.commit()
    conn.close()

def view_article():
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()


    cursor.execute("""
    SELECT * FROM articles LIMIT 3
        
        
        """)

    rows=cursor.fetchall()

    for row in rows:
        print(row)
    
    conn.close()

