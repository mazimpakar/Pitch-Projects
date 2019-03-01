from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    pitchs = db.relationship('Pitch',backref='user',lazy="dynamic")
    comments = db.relationship('Comment',backref='user',lazy="dynamic")
    vote = db.relationship('Vote',backref = 'user',lazy="dynamic")
    categories=db.relationship('PitchCategory',backref = 'user',lazy="dynamic")        
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        reviews = Comment.query.filter_by(pitch_id =id).all()
        return comments
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
        
    
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitchs'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id= db.Column(db.String(255))
    category_id = db.Column(db.String(255))
    comments = db.relationship('Comment',backref='pitch',lazy="dynamic")
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    def save_pitch(self):
        '''
        Function that saves pitches
        '''
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all_pitches(cls):
        '''
        Function that queries the databse and returns all the pitches
        '''
        return Pitch.query.all()

    @classmethod
    def get_pitches_by_category(cls,cat_id):
        '''
        Function that queries the databse and returns pitches based on the
        category passed to it
        '''
        return Pitch.query.filter_by(category_id= cat_id)


    def __repr__(self):
        return f'User {self.name}'

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment= db.Column(db.String)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitchs.id'))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    username =  db.Column(db.String)
    votes= db.Column(db.Integer)
    

    def save_comment(self):
        '''
        Function that saves comments
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        

        return comments

class Vote(db.Model):
    __tablename__ = 'vote'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
   
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    

    def __repr__(self):
        return f'User {self.name}'  
        db.session.add(self)
        db.session.commit()
class PitchCategory(db.Model):
    '''
    Function that defines different categories of pitches
    '''
    __tablename__ ='pitch_categories'


    id = db.Column(db.Integer, primary_key=True)
    name_of_category = db.Column(db.String(255))
    category_description = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    @classmethod
    def get_categories(cls):
        
        categories = PitchCategory.query.all()
        return categories    
if __name__ == '__main__':
    app.manage()         
