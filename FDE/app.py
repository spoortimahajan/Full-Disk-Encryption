from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Default password
PASSWORD = "admin123"

@app.route("/")
def home():
    print("Page Loaded")
    return render_template("index.html")

@app.route("/unlock", methods=["POST"])
def unlock():
    data = request.get_json()
    user_pass = data.get("password")

    if user_pass == PASSWORD:
        return jsonify({"status": "success", "message": "Drive Unlocked... Booting Windows..."})
    else:
        return jsonify({"status": "error", "message": "Incorrect Password!"})

if __name__ == "__main__":
    app.run(debug=True)