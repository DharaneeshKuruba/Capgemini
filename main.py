from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:8888@localhost:3306/jaya"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models after db initialization
from Database.models import User

# Import and register blueprints after models
from API.login import auth_bp
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)
