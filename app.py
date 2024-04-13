import mysql.connector
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345Izo",
            database="izzetcemibik_19070001035_midtermdb"
        )
        if conn.is_connected():
            print('Connected to MySQL database')
        return conn

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

@app.route('/')
def home():
    conn = connect_to_mysql()
    conn.close()  # Bağlantıyı kapat
    return render_template('home.html')

@app.route('/products')
def show_products():
    conn = connect_to_mysql()
    cursor = conn.cursor()

    # Sorgu çalıştırma ve sonuç alma
    query = "SELECT topic, priceToys, imageToys FROM toys WHERE 1=1"
    cursor.execute(query)
    products = cursor.fetchall()

    # Bağlantıyı kapat
    cursor.close()
    conn.close()
    
    return render_template('products.html', products=products)

@app.route('/productdetails/<topic>')
def productdetails(topic):
    conn = connect_to_mysql()
    cursor = conn.cursor(dictionary=True)
    
    # Seçilen ürünü al
    cursor.execute("SELECT * FROM toys WHERE topic=%s", (topic,))
    selected_product = cursor.fetchone()

    if selected_product is None:
        return "Ürün bulunamadı."

    # Ürünün rengini kontrol et
    color = selected_product['colorToys']

    # Boşa alınacak

    # Aynı kategorideki diğer renk seçeneklerini al
    cursor.execute("SELECT * FROM toys WHERE descriptionToys=%s AND colorToys!=%s", (selected_product['descriptionToys'], color))
    other_colors = cursor.fetchall()

    # Bağlantıyı kapat
    cursor.close()
    conn.close()

    return render_template('productdetails.html', product=selected_product, other_colors=other_colors)




@app.route('/go_to_products')
def go_to_products():
    return redirect(url_for('show_products'))

if __name__ == "__main__":
    app.run(debug=True)
