from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app import app, db, login_manager
from models.usuario import Usuario

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuario.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Bienvenido, ' + user.nombre)
            return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrectos.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('Sesión cerrada correctamente.')
    return redirect(url_for('login'))
