from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
def index():    
    return render_template("index.html")    

@app.route("/gallery")
def gallery():

    image_folder = os.path.join(app.static_folder, "img")

    images = []

    for file in os.listdir(image_folder):
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            images.append(file)

    return render_template("gallery.html", images=images)

if __name__ == "__main__":
    app.run(debug=True)