from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    file = request.files.get("file")
    if file:
        filename = file.filename
        key = random.randrange(3, 9)
        encrypted_filename = "CC-" + filename

        file.save(os.path.join("uploads", filename))
        Encrypt(os.path.join("uploads", filename), key)

        return "File Encrypted"
    else:
        return render_template("index.html")

def Encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open("uploads/CC-" + os.path.basename(filename), "wb")
    file.write(data)
    file.close()

if __name__ == '__main__':
    app.run(debug=True, port=5001)