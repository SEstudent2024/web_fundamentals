from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

db_config = {
    'user': 'mysql_assignment_bd',
    'password': 'Mcleanne1624$',
    'host': 'localhost',
}

db = mysql.connector.connect(**db_config)
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Members (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        membership_date DATE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS WorkoutSessions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        member_id INT,
        session_date DATE,
        session_type VARCHAR(100),
        FOREIGN KEY (member_id) REFERENCES Members(id)
    )
''')

@app.route('/members', methods=['POST'])
def add_member():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    membership_date = data.get('membership_date')

    try:
        cursor.execute('INSERT INTO Members (name, email, membership_date) VALUES (%s, %s, %s)', (name, email, membership_date))
        db.commit()
        return jsonify({'message': 'Member added successfully'}), 201
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 400

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    cursor.execute('SELECT * FROM Members WHERE id = %s', (id,))
    member = cursor.fetchone()

    if member:
        return jsonify({'id': member[0], 'name': member[1], 'email': member[2], 'membership_date': member[3]}), 200
    else:
        return jsonify({'error': 'Member not found'}), 404

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.json
    name = data.get('name')
    email = data.get('email')
    membership_date = data.get('membership_date')

    try:
        cursor.execute('UPDATE Members SET name = %s, email = %s, membership_date = %s WHERE id = %s', (name, email, membership_date, id))
        db.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Member not found'}), 404
        return jsonify({'message': 'Member updated successfully'}), 200
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 400

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    try:
        cursor.execute('DELETE FROM Members WHERE id = %s', (id,))
        db.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Member not found'}), 404
        return jsonify({'message': 'Member deleted successfully'}), 200
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 400
    
@app.route('/workouts', methods=['POST'])
def schedule_workout():
    data = request.json
    member_id = data.get('member_id')
    session_date = data.get('session_date')
    session_type = data.get('session_type')

    try:
        cursor.execute('INSERT INTO WorkoutSessions (member_id, session_date, session_type) VALUES (%s, %s, %s)', (member_id, session_date, session_type))
        db.commit()
        return jsonify({'message': 'Workout session scheduled successfully'}), 201
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 400

@app.route('/workouts/<int:id>', methods=['PUT'])
def update_workout(id):
    data = request.json
    session_date = data.get('session_date')
    session_type = data.get('session_type')

    try:
        cursor.execute('UPDATE WorkoutSessions SET session_date = %s, session_type = %s WHERE id = %s', (session_date, session_type, id))
        db.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Workout session not found'}), 404
        return jsonify({'message': 'Workout session updated successfully'}), 200
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 400

@app.route('/members/<int:member_id>/workouts', methods=['GET'])
def get_member_workouts(member_id):
    cursor.execute('SELECT * FROM WorkoutSessions WHERE member_id = %s', (member_id,))
    sessions = cursor.fetchall()

    if sessions:
        return jsonify([{'id': s[0], 'session_date': s[2], 'session_type': s[3]} for s in sessions]), 200
    else:
        return jsonify({'error': 'No workout sessions found for this member'}), 404