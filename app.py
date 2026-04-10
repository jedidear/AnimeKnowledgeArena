from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, ArenaRoom, Question, Choice, Badge

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-123'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'anime_arena.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    top_users = User.query.order_by(User.xp.desc()).limit(5).all()
    rooms = ArenaRoom.query.limit(3).all()
    return render_template('index.html', top_users=top_users, rooms=rooms)

@app.route('/rooms')
def rooms():
    all_rooms = ArenaRoom.query.all()
    return render_template('rooms.html', rooms=all_rooms)
import os
import random

@app.route('/room/<int:room_id>')
@login_required
def room_detail(room_id):
    room = ArenaRoom.query.get_or_404(room_id)
    # Get all questions and shuffle them
    questions = list(room.questions)
    random.shuffle(questions)
    # Take first 20 for the quiz
    questions = questions[:20]

    # Shuffle choices for each question
    for q in questions:
        q.shuffled_choices = list(q.choices)
        random.shuffle(q.shuffled_choices)

    return render_template('quiz.html', room=room, questions=questions)

@app.route('/submit_quiz', methods=['POST'])
@login_required
def submit_quiz():
    data = request.get_json()
    room_id = data.get('room_id')
    answers = data.get('answers')

    correct_count = 0
    total_xp = 0

    for q_id, c_id in answers.items():
        if not c_id: continue
        choice = Choice.query.get(c_id)
        if choice and choice.is_correct:
            correct_count += 1
            total_xp += choice.question.xp_reward

    # Update User Progression
    current_user.xp += total_xp
    current_user.total_score += total_xp
    current_user.update_rank()

    level_up = current_user.calculate_level()

    # Check for first quiz badge
    first_blood = Badge.query.filter_by(name="First Blood").first()
    if first_blood not in current_user.badges:
        current_user.badges.append(first_blood)

    # Check for Quiz Master badge
    if len(answers) >= 20:
        quiz_master = Badge.query.filter_by(name="Quiz Master").first()
        if quiz_master and quiz_master not in current_user.badges:
            current_user.badges.append(quiz_master)

    db.session.commit()

    return jsonify({
        'status': 'success',
        'xp_earned': total_xp,
        'correct': correct_count,
        'new_rank': current_user.rank,
        'new_level': current_user.level,
        'level_up': level_up
    })

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
            
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/leaderboard')
def leaderboard():
    top_users = User.query.order_by(User.xp.desc()).limit(50).all()
    return render_template('leaderboard.html', users=top_users)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
