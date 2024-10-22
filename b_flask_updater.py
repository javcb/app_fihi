from flask import Flask, request, jsonify
from components.db_connection import get_db_connection

app = Flask(__name__)

@app.route('/update_data', methods=['POST'])
def update_data():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Person.Person
        SET FirstName = ?, LastName = ?
        WHERE BusinessEntityID = ?
    """, (data['FirstName'], data['LastName'], data['BusinessEntityID']))
    conn.commit()
    conn.close()
    return jsonify({"message": 