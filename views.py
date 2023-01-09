from flask import render_template, request, redirect

from config import app
from models import Elf, db, UserSite, CategoryElf


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/list-elfs/')
def get_list_elfs():
    return render_template("list_elfs.html")


@app.route('/add-elf/', methods=['POST', 'GET'])
def add_elf():
    if request.method == 'POST':
        name = request.form['name']
        patronymic = request.form['patronymic']
        last_name = request.form['last_name']
        nickname = request.form['nickname']
        quote = request.form['quote']
        date_quote = request.form['date_quote']
        print(name, patronymic, last_name, nickname, quote)

        elf = Elf(
            name=name,
            patronymic=patronymic,
            last_name=last_name,
            nickname=nickname,
            quote=quote,
            date_quote=date_quote
        )
        try:
            db.session.add(elf)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(e)
            return 'error'
    else:
        print('get')
    return render_template("add_elf.html")


@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/admin/')
def admin():
    return render_template("admin.html")


@app.route('/add-user/', methods=['POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        login = request.form['login']
        password = request.form['password']
        email = request.form['email']
        is_active = request.form.get('is-active')
        superuser = request.form.get('superuser')
        moderator = request.form.get('moderator')

        user = UserSite(
            name=name,
            login=login,
            password=password,
            email=email,
            is_active=is_active,
            super_user=superuser,
            moderator=moderator
        )
        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/admin/')
        except Exception as e:
            print(e)
            return 'error'
    return render_template("admin.html")


@app.route('/add-category-elf/', methods=['POST'])
def add_category_elf():
    if request.method == 'POST':
        name = request.form['name-elf-type']

        category_elf = CategoryElf(
            name=name,
        )
        try:
            db.session.add(category_elf)
            db.session.commit()
            return redirect('/admin/')
        except Exception as e:
            print(e)
            return 'error'
    return render_template("admin.html")
