from process import preparation, generate_response
from flask import redirect, Flask, render_template, request

# download nltk
preparation()

# Start Chatbot
app = Flask(__name__)


@app.route("/chatbot")
def home():
    return render_template("chatbot.html")


@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    result = generate_response(user_input)
    return result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/deteksi')
def deteksi():
    return render_template('deteksi.html')


@app.route('/kamus')
def kamus():
    return render_template('dictionary.html')


@app.route('/tentang')
def tentang():
    return render_template('aboutus.html')


if __name__ == "__main__":
    app.run(debug=True)
