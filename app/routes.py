from flask import render_template, request, jsonify
from app import app
from app.workflow import personalize_and_store

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    # Retrieve user input
    user_id = request.form.get('user_id')
    user_input = request.form.get('query')
    
    # Process input and get personalized response
    response = personalize_and_store(user_id, user_input)
    
    return jsonify({'response': response})