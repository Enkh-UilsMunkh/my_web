from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_babel import Babel

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'  # Database configuration
app.config['SECRET_KEY'] = 'mysecretkey'  # Required for Flask-Admin sessions
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default language
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'  # Default timezone

# Initialize database
db = SQLAlchemy(app)

# Initialize Babel for Flask
babel = Babel(app)

# Define a simple User model for the admin panel
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<Role {self.name}>'
# Initialize Flask-Admin
admin = Admin(app, name="My Admin Panel", template_mode="bootstrap3")
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))
# Routes
@app.route('/')
def home():
    greating = "Hi, I am testing my back-end"
    return render_template('index.html', message=greating)

@app.route('/about')
def about():
    f = "I love playing games, and I play piano on the moon"
    return render_template('about.html', message=f)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            # Perform the calculation based on the operation
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2
            else:
                result = "Invalid operation"
        except ValueError:
            result = "Please enter valid numbers."

    return render_template("calculator.html", result=result)


# Create database tables and run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True)
