import os
os.makedirs('templates', exist_ok=True)
sss = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Đoạn này không cần thuộc, hiểu là được -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.1/dist/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
    
    <title>Bai 3</title>
</head>
<body>    
    <div class="container">        
        <p>Chọn một file excel để upload lên server, server sẽ hiển thị nội dung file đó.</p>
        <form action="/" method="post" enctype="multipart/form-data"> <!-- tất cả thông tin muốn đẩy lên sever đều phải để trong form -->
            <div class="row">
                <div class="col-md-9">
                    <input class="form-control w80" type="file" name="file1" id="file1" accept=".xlsx"><!--đặc biệt muốn upload được file cần có enctype="multipart/form-data"-->
                </div>
                <div class="col-md-3">
                    <input class="btn btn-info" type="submit" value="Submit">
                </div>
            </div>
        </form>
    </div>
    
    <div>
        {%if tables%} <!-- đây là jinja 2. giúp đẩy dữ liệu từ server qua -->
            <p>Đây là nội dung của file bạn đã tải lên:</p>
            {{ tables[0]|safe }}  
        {%endif%}
    </div>
    
</body>
</html>
"""
open("templates/index1.html", "w", encoding='utf-8').write(sss)
# End Prepair:-
