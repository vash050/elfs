from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy



from views import app

if __name__ == '__main__':
    app.run(debug=True)
