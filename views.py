from flask import render_template

from config import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/list-elfs/')
def get_list_elfs():
    return render_template("list_elfs.html")


@app.route('/add-elf/')
def add_elf():
    return render_template("add_elf.html")


@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/admin/')
def admin():
    return render_template("admin.html")
