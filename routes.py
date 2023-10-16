from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import User, LearningPath, Question
import random

# This is a simple example of a response generation function
def generate_response(user_question):
    responses = [
        "That's a great question! Here's the answer...",
        "I'm glad you asked! Here's some information...",
        "Here's what I found for your question...",
    ]
    
    response = random.choice(responses)  # Select a random response template
    return f"{response} {user_question}."  # Combine the response with the user's question


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    # Retrieve and display user profile
    return render_template('profile.html')

@app.route('/learning_path')
def learning_path():
    # Generate and display personalized learning path
    return render_template('learning_path.html')

@app.route('/ask_question', methods=['GET', 'POST'])
def ask_question():
    if request.method == 'POST':
        question_text = request.form['question_text']
        if question_text:
            response_text = generate_response(question_text)  # Implement response generation logic
            question = Question(question_text=question_text, response_text=response_text)
            db.session.add(question)
            db.session.commit()
            flash('Your question was submitted successfully!')
        else:
            flash('Please enter a question.')
    return render_template('ask_question.html')

if __name__ == '__main__':
    app.run(debug=True)
