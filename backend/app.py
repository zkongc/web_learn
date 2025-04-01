from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if not user or not user.check_password(data['password']):
        return jsonify({'error': '用户名或密码错误'}), 401

    token = jwt.encode({
        'sub': user.id,
        'exp': datetime.utcnow() + timedelta(days=7)
    }, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({
        'token': token,
        'user_id': user.id,
        'username': user.username
    })

@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        if not data or not data.get('username') or not data.get('password'):
            return jsonify({'error': '用户名和密码不能为空'}), 400
        
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'error': '用户名已存在'}), 409
        
        new_user = User(username=data['username'])
        new_user.set_password(data['password'])
        db.session.add(new_user)
        try:
            db.session.commit()
        except Exception as db_error:
            db.session.rollback()
            return jsonify({'error': f'数据库操作失败: {str(db_error)}'}), 500
        
        return jsonify({
            'message': '注册成功',
            'user_id': new_user.id,
            'username': new_user.username
        }), 201
    except Exception as e:
        return jsonify({'error': '服务器内部错误: ' + str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)