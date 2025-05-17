from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # чтобы React мог обращаться к серверу

@app.route('/api/schedule')
def get_schedule():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, date, time FROM schedule WHERE is_booked = 0')
    slots = [{'id': row[0], 'date': row[1], 'time': row[2]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(slots)

@app.route('/api/book', methods=['POST'])
def book():
    data = request.get_json()
    patient_name = data['patient_name']
    contact = data['contact']
    date, time = data['slot'].split(' ')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO appointments (patient_name, contact, date, time)
    VALUES (?, ?, ?, ?)
    ''', (patient_name, contact, date, time))

    cursor.execute('''
    UPDATE schedule SET is_booked = 1 WHERE date = ? AND time = ?
    ''', (date, time))

    conn.commit()
    conn.close()
    return jsonify({"message": "success"})

if __name__ == '__main__':
    app.run(debug=True)
