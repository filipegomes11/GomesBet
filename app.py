from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

login_manager = LoginManager()
login_manager.init_app(app)

# Usuário "mock" para fins de exemplo
class User:
    def __init__(self, id):
        self.id = id

users = {'1': User('1')}  # Usuário com ID '1' para fins de exemplo

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user = users.get(user_id)
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return 'Usuário inválido'
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Aqui você deve adicionar a lógica para processar o formulário de registro
        # e criar um novo usuário no seu sistema
        username = request.form['username']
        password = request.form['password']
        # Outros campos do formulário de registro...

        # Aqui você pode adicionar a lógica para salvar os dados do novo usuário no banco de dados ou em algum outro meio de armazenamento

        return redirect(url_for('login'))
    
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
