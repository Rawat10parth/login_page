from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="user"
)


@app.route('/')
def signup():
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def signup_submit():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password')

            cursor = db.cursor()
            cursor.execute("INSERT INTO user_details (Username, Password) VALUES (%s, %s)", (username, password))
            db.commit()  # Commit the transaction
            cursor.close()

            return "Signup successful"
        except Exception as e:
            return f"An error occurred: {e}", 500


if __name__ == '__main__':
    app.run(debug=True)
