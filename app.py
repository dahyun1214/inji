from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# 업로드 폴더 생성
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# app.config에 직접 할당
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 파일 목록을 반환하는 함수
def get_uploaded_files():
    return os.listdir(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/start')
def start():
    return render_template('start_page.html')

@app.route('/howto')
def howto():
    return render_template('howto.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_files = request.files.getlist('file')

    for file in uploaded_files:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

    return render_template('start_page.html', uploaded_files=get_uploaded_files())

if __name__ == '__main__':
    app.run(debug=True)