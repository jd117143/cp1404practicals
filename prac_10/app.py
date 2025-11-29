from flask import Flask

app = Flask(__name__)


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<celsius>')
def convert_celsius(celsius):
    celsius_value = float(celsius)
    fahrenheit = convert_celsius_to_fahrenheit(celsius_value)
    return f"{fahrenheit:.2f}"


@app.route('/c/<fahrenheit>')
def convert_fahrenheit(fahrenheit):
    fahrenheit_value = float(fahrenheit)
    celsius = convert_fahrenheit_to_celsius(fahrenheit_value)
    return f"{celsius:.2f}"


if __name__ == '__main__':
    app.run()
