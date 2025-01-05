
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def home ():
    greating = "Hi, I am testing my back-end"
    return render_template('index.html', message = greating)


@app.route('/about')
def about ():
    return render_template('about.html')

#test github
@app.route('/contact')
def contact ():
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

if __name__ == '__main__':
    app.run(debug=True)