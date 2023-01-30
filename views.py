from distutils.util import strtobool

from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash

from config import app
from models import Elf, db, UserSite, CategoryElf


@app.route('/')
def index():
    context = {
        'category_elfs': CategoryElf.query.limit(3).all(),
        'elfs': Elf.query.limit(4).all()
    }
    return render_template("index.html", context=context)


@app.route('/list-elfs/')
def get_list_elfs():
    context = {
        'category_elfs': CategoryElf.query.limit(3).all(),
        'elfs': Elf.query.limit(3).all()
    }
    return render_template("list_elfs.html", context=context)


@app.route('/list-elfs/<string:category_name>')
def get_list_elfs_with_category(category_name):
    context = {
        'category_elfs': CategoryElf.query.limit(3).all(),
        'elfs': Elf.query.filter_by(category_elf=category_name).limit(3).all()
    }
    return render_template("list_elfs.html", context=context)


@app.route('/add-elf/', methods=['POST', 'GET'])
def add_elf():
    if request.method == 'POST':
        try:
            print(request.form)
            name = request.form['name']
            patronymic = request.form['patronymic']
            last_name = request.form['last_name']
            nickname = request.form['nickname']
            quote = request.form['quote']
            date_quote = request.form['date_quote']
            category_elf = request.form['category_elf']
            print(category_elf)

            elf = Elf(
                name=name,
                patronymic=patronymic,
                last_name=last_name,
                nickname=nickname,
                category_elf=category_elf,
                quote=quote,
                date_quote=date_quote
            )

            db.session.add(elf)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(e)
            return 'error'

    else:
        context = {'category_elfs': CategoryElf.query.all()}

        return render_template("add_elf.html", context=context)


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
        password = generate_password_hash(request.form['password'])
        email = request.form['email']
        is_active = bool(request.form.get('is-active'))
        superuser = bool(request.form.get('superuser'))
        moderator = bool(request.form.get('moderator'))

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
            db.session.rollback()
            print(e)
            return redirect('/admin/')
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
            db.session.rollback()
            print(e)
            return redirect('/admin/')
    return render_template("admin.html")


@app.route('/elf/<int:elf_id>')
def get_elf(elf_id):
    context = {
        'category_elfs': CategoryElf.query.limit(3).all(),
        'elf': Elf.query.filter_by(id=elf_id).one()
    }
    return render_template("elf.html", context=context)
