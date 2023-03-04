import base64
import io
import pandas as pd
import qrcode
from flask import Flask, render_template

app = Flask(__name__)

# Đọc DataFrame từ file CSV và tạo mã QR cho giá trị đầu tiên trong cột 'data_column'
df = pd.read_csv('D:\Hiep\web_flask\csv\ex_table3.csv')
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(df['BROADCOM MODEL'].iloc[0])
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Chuyển đổi ảnh QR thành mã PR
buffered = io.BytesIO()
img.save(buffered, format="PNG")
encoded_string = base64.b64encode(buffered.getvalue()).decode('utf-8')

@app.route('/')
def home():
    # Trả về template HTML với mã QR được hiển thị
    return render_template('index1.html', qr_code=encoded_string)

if __name__ == '__main__':
    app.run(debug=True)
