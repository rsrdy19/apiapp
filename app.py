from flask import Flask, render_template, request, jsonify
import sqlite3 as sql
import json

app = Flask(__name__)

# @app.route('/users/<idl>/')
# def test(idl=None):
#     g.db = connect_db()
#     cur = g.db.execute('select id, name from users where id = ?', [idl])
#     rows = cur.fetchall();
#     #der = [dict(id=row[0], posts=row[1]) for row in cur.fetchall()]
#     g.db.close()
#     return render_template('test.html', rows=rows)
#
#
# def connect_db():
#     return sqlite3.connect('users.db')

@app.route('/', methods=["GET"])
def liist():
    con = sql.connect("users.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from users")
    
    d = cur.fetchall();
    print(jsonify(d))
    return jsonify(d)

if __name__ == '__main__':
    app.run(debug = True)
