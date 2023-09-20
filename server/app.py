from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 

# Initialize SQLAlchmigrate = Migrate(app, db)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

db.init_app(app)

api = Api(app)

class Plants(Resource):
    pass

class PlantByID(Resource):
    pass
        

if __name__ == "__main__":
    app.run()