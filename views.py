import os
from distutils.util import strtobool

from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename

from config import app, ALLOWED_EXTENSIONS
from models import Elf, db, UserSite, CategoryElf


def allowed_file(filename):
    """ Функция проверки расширения файла """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
        # проверим, передается ли в запросе файл
        if 'file' not in request.files:
            # После перенаправления на страницу загрузки
            # покажем сообщение пользователю
            flash('Не могу прочитать файл')
            return redirect(request.url)
        file = request.files['file']
        # Если файл не выбран, то браузер может
        # отправить пустой файл без имени.
        if file.filename == '':
            flash('Нет выбранного файла')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # безопасно извлекаем оригинальное имя файла
            filename = secure_filename(file.filename)

            # сохраняем файл
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # если все прошло успешно, то перенаправляем
            # на функцию-представление `download_file`
            # для скачивания файла

        category_elf = CategoryElf(
            name=name,
            img=filename
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
