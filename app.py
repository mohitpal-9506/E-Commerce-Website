from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)
@app.route('/')
def home():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mohit",
        database="ecommerce_db"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    conn.close()

    return render_template(
        "index.html",
        products=products
    )

if __name__ == '__main__':
    app.run(debug=True)
