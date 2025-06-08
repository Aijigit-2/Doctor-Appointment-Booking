from flask import Flask, request, send_file
from flask_cors import CORS
import qrcode
import io

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])
if __name__ == '__main__':
    app.run(debug=True, port=5000)

@app.route('/qr')
def generate_qr():
    data = request.args.get('data')
    if not data:
        return "Пожалуйста, укажите параметр ?data=...", 400

    img = qrcode.make(data)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
