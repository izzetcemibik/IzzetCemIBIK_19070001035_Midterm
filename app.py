import mysql.connector
from flask import Flask, render_template

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
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)

