from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def index():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM submissions')
    submissions = cursor.fetchall()
    data=submissions
    column1_sum = sum(row[3] for row in data)
    column2_sum = sum(row[4] for row in data)
    column1_avg = column1_sum / len(data)
    column2_avg = column2_sum / len(data)
    x=len(data)
    row_sums = [sum(row[3:]) for row in data]
    conn.close()
    return render_template('index.html', submissions=submissions,column1_sum=column1_sum,column2_sum=column2_sum,column1_avg=column1_avg,column2_avg=column2_avg,row_sums=row_sums,x=x)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        fullname = request.form['fullname']
        suggest = request.form['suggest']
        rating = request.form['rating']
        coming = request.form['coming']
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO submissions (fullname, suggest, rating,coming) VALUES (?, ?, ?, ?)',
                       (fullname, suggest, rating,coming))
        conn.commit()
        conn.close()
        flash('Code submitted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=["GET"])
def delete(id):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()#
    cur.execute("DELETE FROM submissions WHERE id=?", (id,))
    conn.commit()
    conn.close()
    flash("data was delete successfully")
    return redirect( url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)