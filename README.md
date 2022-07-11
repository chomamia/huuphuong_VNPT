# **BÁO CÁO THỰC TẬP TUẦN 2** 

## **I. Nhiệm vụ** ##
|      Ngày     |      Nhiệm vụ                                                     |
| :------------:|:-----------------------------------------------------------------:|
|    Thứ hai    |      Ôn tập kiến thức về Python                                   |
|    Thứ ba     |      Tìm hiểu về Pipenv và cách thực hiện                          |
|    Thứ tư     |      Thao tác với cơ sở dữ liệu SQLite và phân biệt SQL với noSQL |
|    Thứ năm    |      Tìm hiểu về Git                                              |
|    Thứ sáu    |      Tìm hiểu về Git                                              |  
  
## **II. Nội dung báo cáo**.
### **1. Kiến thức cơ bản về Python**
Ôn tập kiến thức cơ bản về Python và một số nhiệm vụ có liên quan. 
### **2. Tìm hiểu về tạo môi trường Pipenv**
#### **2.1 Giới thiệu về Pipenv**
Pipenv là công cụ quản lý gói kết hợp chức năng của Pip và Virtualenv, cùngvớicác tính năng tốt nhất của các công cụ đóng gói từ các ngôn ngữ hác như 
Bundler và NPM. Điều này dẫn đến một quy trình công việc đơn giản hóa để cài đặt cácgói vàquản lý môi trường ảo.  

**Các vấn đề mà Pipenv cần giải quyết:**
- Không còn cần phải sử dụng pip và virtualenv riêng biệt. 
- Việc quản lý tệp requirements.txt có thể có vấn đề, vì vậy PipenvsửdụngPipfile và Pipfile.lock để tách các khai báo phụ thuộc trừu tượng khỏi kết hợp
được thử nghiệm cuối cùng.
- Hash được sử dụng ở mọi nơi, mọi lúc. An toàn
- Khuyến khích mạnh mẽ việc sử dụng các phiên bản phụ thuộc mới nhất đểgiảm thiểu rủi ro bảo mật phát sinh từ các thành phần lỗi thời.  
#### **2.2 Một số các thao tác cơ bản trên Pipenv**
-Cài đặt môi trường ảo Pipenv:       *$pip install pipenv*  
-Tạo môi trường ảo cho từng project: *$pipev install*  
-Cài đặt các thư viện:               *$pipenv install name_library*  
-Kích hoạt môi trường để sử dụng:    *$pipenv shell*  
-Tạo file requirement:               *$pipenv lock -r requirements.txt* 
### **3. Tìm hiểu về cơ sở dữ liệu SQLite**
#### **3.1 Giới thiệu về SQLite**
SQLite là một hệ quản trị cơ sở dữ liệu hay còn gọi là hệ thống cơ sở dữ liệu quan hệ nhỏ gọn, khác với các hệ quản trị khác như MySQL, SQL Server, 
Ocracle,PostgreSQL… SQLite là một thư viện phần mềm mà triển khai một SQLDatabaseEngine truyền thống, không cần mô hình client-server nên rất nhỏ gọn. 
#### **3.2 Một số thao tác vơ bản về SQLite**
-Tạo ra một cơ sở dữ liệu.  
-Tạo bảng trong cơ sở dữ liệu.  
-Ghi dữ liệu vào cơ sở dữ liệu.  
-Lấy dữ liệu ra từ cơ sở dữ liệu.  
-Chỉnh sửa cơ sở dữ liệu.  
-Xoá cơ sở dữ liệu.  
#### **3.3 Ví dụ về câu lệnh.**
-Các câu lệnh thực hiện có thể trình bày ở đây.  
#### **3.4 So sánh giữa SQL và noSQL.**
SQL là hệ cơ sở dữ liệu được lưu trữ theo dạng bảng, có quan hệ rõ ràng và yêu cầu cao về phần cứng.  
NoSQL là hệ cơ sở dữ liệu phân tán, không ràng buộc, có thể chứa hàng petabytes, độ chịu tải cao và không yêu cầu về tài nguyên phần cứng.  
|    Tính năng     |      SQL                                                    | noSQL|
| :------------:|:-----------------------------------------------------------------:|:------------:|
|   Hiệu suất    |      Khi truy vấn phải tính toán và kiểm tra các mối quan hệ  | Bỏ qua các ràng buộc |
|    Tốc độ   |       Nếu sử dụng quá nhiều server phải bảo toàn tính nhất quán về dữ liệu ở các server với nhau | Xử lí nhanh hơn vì bỏ qua các cơ chế ràng buộc |
|    Phần cứng    |     Đòi hỏi về mặt phần cứng cao  | Không đòi hỏi về mặt phần cứng |
|    Truy vấn và báo cáo    |    Dễ dàng sử dụng ngôn ngữ SQL query để truy vấn trực tiếp dữ liệu từ database hoặc dùng công cụ hỗ trợ để lấy báo cáo | Việc lấy báo cáo dữliệutrựctiếptừ NoSQL chưa được hỗtrợtốtthực hiện chủ yếu thôngquagiaodiện ứng dụng.|
|    Mở rộng dữ liệu    | Khi muốn bổ sung dữ liệu cột cho bảng, phải khai báo trước| Không còn báo cáo trước.   |  
| Ứng dụng | Sử dụng để xây dựng những hệ thống có quan hệ chặt chẽ và cần tính đồng nhất về dữ liệu như: tài chính, ngân hàng, chứng khoán,…| Sử dụng xây dựng nhữnghệthốnglưu trữ thông tin lớn, khôngquáquan trọng về đồng nhất dữliệutrong một thời gian nhất địnhnhưbáo chí, mạng xã hội, diễnđàn,…|  

### **4. Git**
#### **4.1 Giới thiệu về Git**  
Git là hệ thống kiểm soát phiên bản phân tán mà nguồn mở. Các dự án thực tế thường có nhiều nhà phát triển làm việc song song. Vì vậy, một hệ thống kiểm soát phiên bản như Git là cần thiết để đảm bảo không có xung đột mã giữa các nhà phát triển. Ngoài ra, các yêu cầu trong dự án thay đổi thường xuyên. Vì vậy, cần một hệ thống cho phép nhà phát triển quay lại phiên bản cũ hơn của mã.  
**Repository** là nơi chứa tất cả mã nguồn cho một dự án được tạo bởi Git. Hoặc có thể hiểu Repository chính khai báo thư mục chứa dự án của bạn trên local
hoặc remote. Một repository sẽ có hai cấu trúc dữ liệu chính đó là Object store và Index được lưu trữ ẩn trong thư mục .git.  
Có hai loại repository là:local repository và remote repository: 
- **Local repository**: là repository được cài đặt trên máy tính của lập trình viên, repository này sẽ đồng bộ hóa với 
remote bằng các lệnh của Git. 
- **Remote repository**: là repository được cài đặt trên server chuyên dụng, điển hình hiện nay là Github.  Branch là những phân
nhánh ghi lại luồng thay đổi của lịch sử, các hoạt động trên mỗi branch sẽ không ảnh hưởng lên các branch khác nên có thể tiến hành nhiều thay đổi đồng thời 
trên một repository giúp giải quyết nhiều nhiệm vụ cùng lúc. Khi tạo một repository thì Git sẽ thiết lập branch mặc định là master.  
#### **4.2  Một số câu lệnh cơ bản của Git**
-Cấu hình tên tài khoản trên local: *git config –global user.name [username].*  
-Cấu hình email trên local: *git config -global user.email [youremail]*.  
-Tải source về local đang gọi : *git clone [url]*.  
-Tạo kết nối trên local: *git init*.  
-Thêm các file cần tải lên vào index: *git add [namefile]*.  
-Tạo commit từ local với sever: *git commit -m "message"*.  
-Tạo nhánh mới: *git branch [namebranch]*.  
-Truy cập vào nhánh: *git checkout [namebranch]*.  
-Gộp nhánh: *git merge*
-Tải soure: *git pull*
-Tạo kết nối với server: *git remote add origin [url]*.  
-Tải source từ local lên server: *git push -u origin [namebranch]*.

