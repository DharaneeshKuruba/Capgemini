from flask import Flask
from .API.login import auth_bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root123@localhost:3306/captest"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register blueprint
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)