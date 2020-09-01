from amazon.save_date import conn

cor = conn.cursor()
cor.execute("SELECT * FROM Reviews")
result = cor.fetchall()
print(len(result))
conn.close()
