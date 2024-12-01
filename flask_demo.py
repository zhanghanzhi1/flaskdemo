from flask import Flask

app = Flask(__name__)

# Basic greeting route that returns "Hello World" with an HTML tag
@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

# Dynamic greeting route that can include a name or just say "Hello"
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    if name:
        return f'<h1>Hello, {name}!</h1>'
    else:
        return '<h1>Hello!</h1>'

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Route to perform temperature conversion from Celsius to Fahrenheit
@app.route('/convert/<float:celsius>')
def convert_temperature(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    return f'{celsius}°C is equivalent to {fahrenheit}°F'

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)
