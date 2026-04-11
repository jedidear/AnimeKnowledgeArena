from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

# Association table for User-Badge relationship
user_badges = db.Table('user_badges',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('badge_id', db.Integer, db.ForeignKey('badges.id'), primary_key=True)
)

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    profile_image = db.Column(db.String(256), default='default.jpg')
    
    # Progression Stats
    xp = db.Column(db.Integer, default=0)
    level = db.Column(db.Integer, default=1)
    rank = db.Column(db.String(64), default='Academy Student')
    total_score = db.Column(db.Integer, default=0)
    
    def calculate_level(self):
        # Level = floor(sqrt(XP/100)) + 1
        import math
        new_level = math.floor(math.sqrt(self.xp / 100)) + 1
        if new_level > self.level:
            self.level = new_level
            return True # Levelled up
        return False

    def xp_to_next_level(self):
        # XP required for level N+1 is ((N)^2) * 100
        return (self.level ** 2) * 100

    def progress_percentage(self):
        prev_xp = ((self.level - 1) ** 2) * 100 if self.level > 1 else 0
        next_xp = (self.level ** 2) * 100
        return min(100, int(((self.xp - prev_xp) / (next_xp - prev_xp)) * 100))
    
    # Relationships
    badges = db.relationship('Badge', secondary=user_badges, backref=db.backref('users', lazy='dynamic'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def update_rank(self):
        # Automated rank system based on XP
        if self.xp > 5000: self.rank = "Legendary Sannin"
        elif self.xp > 2000: self.rank = "Jonin"
        elif self.xp > 1000: self.rank = "Chunin"
        elif self.xp > 500: self.rank = "Genin"
        else: self.rank = "Academy Student"

    def __repr__(self):
        return f'<User {self.username}>'

class ArenaRoom(db.Model):
    __tablename__ = 'arena_rooms'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    anime_title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(256))
    questions = db.relationship('Question', backref='room', lazy=True)

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('arena_rooms.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    xp_reward = db.Column(db.Integer, default=50)
    choices = db.relationship('Choice', backref='question', lazy=True)

class Choice(db.Model):
    __tablename__ = 'choices'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    is_correct = db.Column(db.Boolean, default=False)

class Badge(db.Model):
    __tablename__ = 'badges'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(256))
    icon = db.Column(db.String(64)) # FontAwesome icon name
