from flask import Flask, render_template, request
import pymysql 
import sys

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host = '127.0.0.1',
        user= 'randomuser',
        password='randompassword08',
        database= 'db_registrarr',
        cursorclass=pymysql.cursors.DictCursor

    )

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        birth_date = request.form.get("birth_date")
        print(f"{first_name}, {last_name},{birth_date},{email}", file=sys.stderr)

        name = f"{first_name}{last_name}"


    
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO tbl_student (first_name, last_name, birth_date, email)
                VALUES (%s,%s,%s,%s)

            """
            cursor.execute(sql,(first_name,last_name,birth_date,email))
        connection.commit()
     

        connection.close()

        # Here you could save data or process it
        return render_template("form.html", submitted=True, first_name=first_name, last_name=last_name, birth_date = birth_date, email=email)

    return render_template("form.html", submitted=False)


if __name__ == "__main__":
    app.run(debug=True)
