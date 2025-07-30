from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['image']
        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)

        # Aqui você colocaria a lógica de face swap
        # Por enquanto, só mostra a imagem original
        return render_template('index.html', image_path=image_path)

    return render_template('index.html', image_path=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
