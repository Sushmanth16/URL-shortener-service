import string
import random
from flask import Flask, request, redirect, render_template, jsonify

app = Flask(__name__)

url_store = {}

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None
    if request.method == "POST":
        original_url = request.form.get("url")
        if original_url:
            code = generate_code()
            while code in url_store:
                code = generate_code()
            url_store[code] = original_url
            short_url = request.host_url + code
    return render_template("index.html", short_url=short_url)

@app.route("/api/shorten", methods=["POST"])
def shorten():
    data = request.get_json()
    original_url = data.get("url")
    if not original_url:
        return jsonify({"error": "URL is required"}), 400

    code = generate_code()
    while code in url_store:
        code = generate_code()

    url_store[code] = original_url
    return jsonify({
        "original_url": original_url,
        "short_code": code,
        "short_url": request.host_url + code
    })

@app.route("/<code>")
def redirect_to_url(code):
    original_url = url_store.get(code)
    if original_url:
        return redirect(original_url)
    return "Short URL not found", 404

if __name__ == "__main__":
    app.run(debug=True)
