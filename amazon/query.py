from amazon.save_date import conn

cor = conn.cursor()
cor.execute("SELECT * FROM Topsellers")
result1 = cor.fetchall()
cor.execute("SELECT * FROM Reviews")
result2 = cor.fetchall()
print("Topselers:{}".format(len(result1)))
print("Reviews:{}".format(len(result2)))

cor.execute("SELECT * FROM TopSellers WHERE ASIN = ?", ("B00002N8CX",))
cor.fetchone()
