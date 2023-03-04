
from flask import Flask, render_template, request
import pandas as pd
from docx import Document
import io,csv
from model import *
import os
app = Flask(__name__)

def read_docx_tables(filename, tab_id=None):
    def read_docx_tab(tab):
        with io.StringIO() as vf:
            writer = csv.writer(vf)
            for row in tab.rows:
                writer.writerow(cell.text for cell in row.cells)
            vf.seek(0)
            df = pd.read_csv(vf)
            return df

    doc = Document(filename)
    tables = doc.tables
    if tab_id is not None:
        if tab_id < len(tables):
            return read_docx_tab(tables[tab_id])
        else:
            print("Error: Specified [tab_id]: {} does not exist.".format(tab_id))
    else:
        return [read_docx_tab(tab) for tab in tables]

@app.route('/', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        # Lấy tệp và lưu vào thư mục upload_dir
        file = request.files['file1']
        upload_dir = f"data/ProjectName/{request.environ['REMOTE_ADDR']}"
        os.makedirs(upload_dir, exist_ok=True)
        file_path = os.path.join(upload_dir, file.filename)
        file.save(file_path)

        # Đọc và chuyển đổi các bảng dữ liệu
        df = read_docx_tables(file_path)
        tb1, tb2, tb3 = (table1(df[0]), table2(df[1]), chuyen_tb3(df[2]))

        # Chuyển đổi các bảng dữ liệu thành HTML và trả về
        return render_template('index3.html', tables=[
            tb1.to_html(classes='table table-hover', index=False, table_id='tb1-resuly'),
            tb2.to_html(classes='table table-hover', index=False, table_id='tb2-resuly'),
            tb3.to_html(classes='table table-hover', header=False, table_id='tb3-resuly')
        ])

    # Trả về trang web mặc định
    return render_template('index3.html')

if __name__=='__main__':
    app.run(debug=True ,port= 2346,host='0.0.0.0')