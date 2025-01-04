from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from controllers.user import add_user_function, edit_user_function, delete_user_function
from functools import wraps
import sys
from models.user import User

main = Blueprint('main', __name__)

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('main.login'))
        return f(*args, **kwargs)
    return decorated_function

@main.route('/login', methods=['GET', 'POST'])
def login():
    # Cek jika user sudah login
    if 'user_id' in session:
        return redirect(url_for('main.home'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.password == password:  # Dalam produksi, gunakan password hashing!
            session['user_id'] = user.id
            session['user_email'] = user.email  # Simpan email user di session
            flash('Selamat datang kembali!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Email atau password salah', 'error')
            return render_template('login.html')
            
    return render_template('login.html')

@main.route('/logout')
def logout():
    # Hapus semua data session
    session.clear()
    flash('Anda telah berhasil logout', 'success')
    return redirect(url_for('main.login'))

# Tambahkan decorator login_required ke rute yang membutuhkan autentikasi
@main.route('/', methods=['GET', 'POST'])
@login_required
def home():
    data = User.get_all()
    return render_template('index.html', data=data)

@main.route('/adduser', methods=['GET','POST'])
@login_required
def add_user():
    data = add_user_function()
    print(data,file=sys.stderr)
    return render_template('adduser.html', data=data)

@main.route('/edituser/<int:id>', methods=['GET','POST'])
@login_required
def edit_user(id):
    user = User.get_by_id(id)
    if request.method == "POST":
        data = edit_user_function(user)
        return redirect(url_for('main.home'))
    return render_template('edituser.html', user=user)

@main.route('/deleteuser/<int:id>', methods=['POST'])
@login_required
def delete_user(id):
    user = User.get_by_id(id)
    print(user, file=sys.stderr)
    delete_user_function(user)
    return redirect(url_for('main.home'))
