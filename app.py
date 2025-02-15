from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Не забудьте изменить это на что-то более безопасное!

# Простая база данных в виде списка для хранения пользователей (в реальном проекте используйте базу данных)
users = []

@app.route('/')
def index():
    return "Welcome to My Messenger!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form.get('last_name', '')  # Фамилия необязательна
        username = request.form['username']

        # Проверка уникальности имени пользователя
        if any(user['username'] == username for user in users):
            flash('Username already exists. Please choose another one.')
            return redirect(url_for('register'))

        users.append({'first_name': first_name, 'last_name': last_name, 'username': username})
        flash('Registration successful!')
        return redirect(url_for('index'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)