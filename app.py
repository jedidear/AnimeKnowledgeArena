import os
import traceback
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, ArenaRoom, Question, Choice, Badge

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-123')
basedir = os.path.abspath(os.path.dirname(__file__))

# Priority: External Database URL -> Local SQLite
db_url = os.environ.get('DATABASE_URL')
if db_url and db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

try:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url or 'sqlite:///' + os.path.join(basedir, 'anime_arena.db')    
except Exception as e:
    print(f"⚠️ Database URL failed, falling back to local: {e}")
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
    try:
        top_users = User.query.order_by(User.xp.desc()).limit(5).all()
        rooms = ArenaRoom.query.limit(3).all()
        return render_template('index.html', top_users=top_users, rooms=rooms)
    except Exception as e:
        print(f"Error in index: {e}")
        return render_template('index.html', top_users=[], rooms=[])

@app.route('/rooms')
def rooms():
    all_rooms = ArenaRoom.query.all()
    return render_template('rooms.html', rooms=all_rooms)

@app.route('/room/<int:room_id>')
@login_required
def room_detail(room_id):
    room = ArenaRoom.query.get_or_404(room_id)
    import random
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
    try:
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
    except Exception as e:
        db.session.rollback()
        print(f"Quiz Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user)
                return jsonify({'status': 'success', 'redirect': url_for('index')})
            return jsonify({'status': 'error', 'message': 'Invalid username or password'}), 401
        except Exception as e:
            print(f"Login Error: {e}")
            return jsonify({'status': 'error', 'message': 'Internal Server Error'}), 500
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')

            if not username or not email or not password:
                return jsonify({'status': 'error', 'message': 'All fields are required'}), 400

            if User.query.filter_by(username=username).first():
                return jsonify({'status': 'error', 'message': 'Username already exists'}), 400
            
            if User.query.filter_by(email=email).first():
                return jsonify({'status': 'error', 'message': 'Email already exists'}), 400

            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Account created!', 'redirect': url_for('login')})      
        except Exception as e:
            db.session.rollback()
            print("--- REGISTER ERROR START ---")
            print(traceback.format_exc())
            print("--- REGISTER ERROR END ---")
            return jsonify({'status': 'error', 'message': f'Database/Server Error: {str(e)}'}), 500
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

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

def auto_seed():
    try:
        if ArenaRoom.query.first() is None:
            print("🌱 Auto-seeding database...")
            from data_seed import BADGES_DATA, ROOMS_DATA, NARUTO_QUESTIONS, ONE_PIECE_QUESTIONS, AOT_QUESTIONS     

            # 1. Sync Badges
            for b_data in BADGES_DATA:
                if not Badge.query.filter_by(name=b_data["name"]).first():
                    db.session.add(Badge(name=b_data["name"], description=b_data["desc"], icon=b_data["icon"]))     

            # 2. Sync Rooms
            for r_data in ROOMS_DATA:
                if not ArenaRoom.query.filter_by(name=r_data["name"]).first():
                    room = ArenaRoom(name=r_data["name"], anime_title=r_data["anime"], description=r_data["desc"], image_url=r_data["img"])
                    db.session.add(room)
            db.session.commit()

            # 3. Add Questions
            def add_qs(room_name, questions_list):
                room = ArenaRoom.query.filter_by(name=room_name).first()
                if not room: return
                for q_text, choices in questions_list:
                    if not Question.query.filter_by(text=q_text, room_id=room.id).first():
                        q = Question(room_id=room.id, text=q_text, xp_reward=100)
                        db.session.add(q)
                        db.session.commit()
                        for c_text, is_corr in choices:
                            db.session.add(Choice(question_id=q.id, text=c_text, is_correct=is_corr))
                        db.session.commit()

            add_qs("Hidden Leaf Village", NARUTO_QUESTIONS)
            add_qs("The Grand Line", ONE_PIECE_QUESTIONS)
            add_qs("Shiganshina District", AOT_QUESTIONS)
            print("🔥 Database seeded successfully!")
    except Exception as e:
        print(f"Seeding Error: {e}")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        auto_seed()
    app.run(debug=True)
else:
    with app.app_context():
        db.create_all()
        auto_seed()
