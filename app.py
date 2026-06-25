from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)
@app.route('/')
def home():

   products = [
    (1, "Shirt", 999, "shirt.jpg"),
    (2, "Shoes", 1999, "shoes.jpg"),
    (3, "Watch", 1499, "watch.jpg")
]

   return render_template("index.html", products=products)

if __name__ == '__main__':
    app.run(debug=True)
