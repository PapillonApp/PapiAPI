from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
from datetime import datetime

app = Flask(__name__)
messages_file = 'messages.json'


def read_messages():
    try:
        with open(messages_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def write_messages(messages):
    with open(messages_file, 'w') as f:
        json.dump(messages, f, indent=4)


@app.route('/')
def home():
    messages = read_messages()
    return render_template('index.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    messages = read_messages()
    new_message = {
        "id": len(messages) + 1,
        "enabled": request.form.get('enabled', 'false') == 'true',
        "message": request.form['message'],
        "date": datetime.now().strftime("%Y-%m-%d"),
        "importance": int(request.form['importance']),
        "type": request.form['type']
    }
    messages.append(new_message)
    write_messages(messages)
    return redirect(url_for('home'))


@app.route('/toggle_message/<int:message_id>', methods=['POST'])
def toggle_message(message_id):
    messages = read_messages()
    for message in messages:
        if message['id'] == message_id:
            message['enabled'] = not message['enabled']
            continue
        message['enabled'] = False
    write_messages(messages)
    return redirect(url_for('home'))


@app.route('/delete_message/<int:message_id>', methods=['POST'])
def delete_message(message_id):
    messages = read_messages()
    messages = [m for m in messages if m["id"] != message_id]
    write_messages(messages)
    return redirect(url_for('home'))


@app.route('/edit_message/<int:message_id>', methods=['POST'])
def edit_message(message_id):
    messages = read_messages()
    for message in messages:
        if message['id'] == message_id:
            message['message'] = request.form['message']
            message['importance'] = int(request.form['importance'])
            break
    write_messages(messages)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
