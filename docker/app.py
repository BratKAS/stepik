from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/button_click', methods=['POST'])
def button_click():
    return "Вы нажали кнопку!"


if __name__ == '__main__':
    app.run(debug=True)
