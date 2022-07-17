# **Báo cáo thực tập tuần 3**

## **I.Nhiệm vụ của tuần 3**
|      Ngày     |      Nhiệm vụ                                                     |
| :------------:|:-----------------------------------------------------------------:|
|    Thứ hai    |      Tìm hiểu và áp dụng framework Flask                                  |
|    Thứ ba     |      Tìm hiểu và áp dụng framework Flask                           |
|    Thứ tư     |      Viết API sử dụng Flask và gửi email từ Python |
|    Thứ năm    |      Tìm hiểu và chạy thử dự án nhỏ Flask và SQLite                   |
|    Thứ sáu    |       Tìm hiểu và chạy thử dự án nhỏ Flask và SQLite                |  

## **II.Nội dung báo cáo** ##
### **1.Tìm hiểu về Framework Flask**
  Flask là một web frameworks, nó thuộc loại micro-framework được xây dựng bằng ngôn ngữ lập trình Python. Flask cho phép bạn xây dựng các ứng dụng web từ  
đơn giản tới phức tạp. Nó có thể xây dựng các api nhỏ, ứng dụng web chẳng hạn như các trang web, blog, trang wiki hoặc một website dựa theo thời gian hay  
thậm chí là một trang web thương mại. Flask cung cấp cho bạn công cụ, các thư viện và các công nghệ hỗ trợ bạn làm những công việc trên.  
  Flask là một micro-framework. Điều này có nghĩa Flask là một môi trường độc lập, ít sử dụng các thư viện khác bên ngoài.  Do vậy, Flask có ưu điểm là   
nhẹ, có rất ít lỗi do ít bị phụ thuộc cũng như dễ dàng phát hiện và xử lý các lỗi bảo mật.  
#### **1.1.thư viện có liên quan**  
**SQLAlchemy**  
  SQLAlchemy là một bộ công cụ SQL mã nguồn mở và ORM sử dụng trong ngôn ngữ lập trình Python, giúp hỗ trợ việc quản lý và thao tác với cơ sở dữ liệu.  
SQLAlchemy cung cấp cho người dùng một ORM sử dụng mô hình thiết kế Data Mapper.  
Được ra lò vào năm 2006, SQLAlchemy nhanh chóng khẳng định vị thế của mình trong cộng đồng lập trình viên Python, được sử dụng rất rộng rãi bên cạnh   
Django’s ORM. SQLAlchemy được sử dụng phổ biến ở cả những “ông lớn” trong ngành công nghệ như Yelp!, Reddit, Dropbox, …

**Marshmallow**  
  Là một thư viện cho phép người dùng có thế thực hiện các thao tác liên quan đến chuyển đổi dữ liệu từ cơ sở dữ liệu thành các kiểu dữ liệu khác nhau  
đặc biệt là file Json.
#### **1.2.Cài đặt Flask và các thư viện liên quan**  
Chúng ta có thể cài đặt Flask bằng Pipenv : *$pipenv install flask*  
Cài đặt SQLAlchemy để quản lý cơ sở dữ liệu: *$pipenv install flask_sqlalchemy*  
Cài đặt Marshmallow để chuyển đổi cơ sở dữ liệu sang Json: *$pipenv install flask_marshamallow*  
Cài đặt thư viện liên quan đến thao tác email: *$pipenv install flask_mail*
#### **1.3.Hoạt động của Flask**
Một ví dụ cơ bản:  
*from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run()*
 
 ở ví dụ trên thì để khởi tạo mội app thì ta dùng: *app = Flask(__name__)*  
 Khởi tạo URL: *@app.route('/')*  
 Để thực hiện các thao tác của đường dẫn ta sử dụng function ở ngay dưới đường đãn được khởi tạo.  
 Để thực hiện khởi chạy thì sử dụng: *app.run()*  
 
 ### **2.Viết API để gửi email từ python**
Cài đặt thư viện liên quan đến thao tác email: *$pipenv install flask_mail*.  
Sau đó chúng ta có thể khai báo địa chỉ email và mật khẩu ứng dụng liên quan đến email nguồn.  
Lấy địa chỉ email của người nhân và nội dung cần gửi bở input.  
Tiến hành gửi email theo nội dung và nguời nhận đã được truyền vào ở trên.  
Source code có thể xem tại [đây](https://github.com/chomamia/huuphuong_VNPT/tree/master/send_email)

 ### **3.Viết API của dự án nhỏ**
Nhiệm vụ: Tạo 1 bảng dữ liệu bao gồm:  
NHANVIEN  
idNhanVien (string) suggest sử dụng uuidv4  
tenNhanVien (string)   
CCCD (string) <- unique (duy nhất)  
email (string) <- unique (duy nhất)  
phone (string) <- unique (duy nhất)  
Đầu ra: 5 APIs, sử dụng Postman để kiểm tra API nha  
1. API danh sách nhân viên Method: GET  
2. API tạo nhân viên: POST -> tạo thành công thì gửi email thông báo đến nhân viên đó  
3. API cập nhật nhân viên Method: POST / PUT  
4. API thông tin nhân viên Method: GET  
5. API xóa nhân viên Method: DELETE  

Được thực hiện theo mô hình Blueprint
Kết quả: Các API đã được hoàn thành và đã được kiểm tra bởi Postman
1. API danh sách nhân viên: URL= */staff-management/staffs* methods = ["GET"]  
2. API tạo nhân viên: URL= */staff-management/staff* methods = ["POST"]   
3. API cập nhật nhân viên Method: URL= */staff-management/staff/<int:id>* methods = ["PUT"]  
4. API thông tin nhân viên Method: URL= */staff-management/staff/<int:id>* methods = ["GET"]  
5. API xóa nhân viên: URL= */staff-management/staff/<int:id>* methods = ["DELETE"]  

Source code có thể xem tại [đây](https://github.com/chomamia/huuphuong_VNPT/tree/master/API_Manage_Staff)
 
 

