=======================================================================================
  Evi Portable — Hướng dẫn sử dụng (tổng quan)
  Tài liệu: Tiếng Anh • Áp dụng cho bản dựng bạn nhận được cùng với thư mục này
=======================================================================================

Đặt các hướng dẫn hoặc bản dịch dài hơn của riêng bạn ở đây (ví dụ: EN_User_Manual.pdf,
DE_Handbuch.txt). Tệp này là tùy chọn để Evi chạy; nó dành cho bạn để đọc
hoặc in ấn.

Bản sao đã bản địa hóa: README_<LANG>.txt và FEHLERSUCHE_<LANG>.txt trong thư mục này
(cùng mã ngôn ngữ với giao diện người dùng trang web). Tổng quan bằng tiếng Anh: README.txt này;
Khắc phục sự cố bằng tiếng Anh: FEHLERSUCHE_EN.txt. Khắc phục sự cố của Đức cũng là
được duy trì bằng tay dưới dạng FEHLERSUCHE_DE.txt.

Chỉ mục thư mục (đặt tên tệp, trình tạo): README.md

--------------------------------------------------------------------------------
  Hệ điều hành
--------------------------------------------------------------------------------

Evi Portable chỉ dành cho Microsoft Windows 10 và Windows 11. Nó không phải
được hỗ trợ trên các hệ điều hành Windows 7/8, macOS, Linux hoặc di động.

--------------------------------------------------------------------------------
  Lần khởi đầu đầu tiên — từ tải xuống đến chạy Evi
--------------------------------------------------------------------------------

1) Vị trí cài đặt
   Sao chép hoặc trích xuất toàn bộ thư mục Evi vào nơi bạn kiểm soát - ví dụ:
   Máy tính để bàn, Tài liệu hoặc thẻ nhớ USB của bạn. Giữ cấu trúc thư mục như
   đã gửi (không xóa các thư mục con mà bạn không tự tạo).

2) Mô hình ngôn ngữ (bắt buộc)
   Evi cần một tệp mô hình AI chính (phần mở rộng .gguf) trong thư mục:
   người mẫu\llm\
   Xem models\llm\README.txt để biết các đề xuất về kích thước. Sau khi tập tin ở đó,
   bắt đầu Evi; nó tự động phát hiện mô hình khi có thể.

3) Lần ra mắt đầu tiên - kích hoạt
   Khi bạn khởi động Evi lần đầu tiên, một cửa sổ kích hoạt sẽ xuất hiện.
   • PC của bạn hiển thị ID máy (duy nhất cho phần cứng này).
   • Sao chép ID máy (nút: "Sao chép ID máy") và gửi qua e-mail đến:
     Brielbeck@hotmail.de
   • Bạn sẽ nhận được khóa nối tiếp chỉ hoạt động trên cùng một PC đó
     (khóa được liên kết với phần cứng của bạn).
   • Dán mã khóa vào cửa sổ kích hoạt và chọn Kích hoạt.

   Nếu bạn thay đổi phần cứng chính hoặc di chuyển đĩa theo cách làm thay đổi ID,
   bạn có thể cần một chìa khóa mới — hãy liên hệ với cùng một địa chỉ.

4) Sau khi kích hoạt
   Cửa sổ chính mở ra. Chọn ngôn ngữ, micrô và giọng nói ở bên trái
   bảng cài đặt. Nói "mở bảng ghi chú" bất cứ lúc nào để biết ví dụ về lệnh
   (xem cheatsheets\en.txt và các tệp chị em để biết các ngôn ngữ khác).

5) Tùy chọn: mở hướng dẫn này từ Windows
   Trong File Explorer, đi tới thư mục Evi, sau đó Manual\README.txt và mở nó
   bằng Notepad hoặc bất kỳ trình xem văn bản nào.

--------------------------------------------------------------------------------
  Ngôn ngữ giao diện (GUI)
--------------------------------------------------------------------------------

Giao diện người dùng tuân theo ngôn ngữ bạn chọn ở phần Ngôn ngữ ở trên cùng
của bảng cài đặt bên trái (khối đầu tiên trong thanh bên). Sau khi bạn chọn một
ngôn ngữ, menu, nút, nhãn và hầu hết văn bản trên màn hình đều chuyển sang ngôn ngữ đó
ngôn ngữ ở bất cứ nơi nào có bản dịch. Bạn có thể thay đổi nó bất cứ lúc nào; chỉ có
thay đổi từ ngữ, không phải cách bố trí.

Mẹo: Các bảng cheat lệnh trong thư mục cheatsheets\ được liệt kê theo
mã ngôn ngữ (en.txt, de.txt,…). Để biết chi tiết, hãy xem cheatsheets\README.txt.
Thư mục Manual\ này là phần tổng quan về sản phẩm dài hơn; tờ cheat là
danh sách "những gì cần nói" nhanh chóng.

--------------------------------------------------------------------------------
  Card đồ họa (GPU) - hướng dẫn nhanh
--------------------------------------------------------------------------------

Một lựa chọn ở giữa mạnh mẽ là NVIDIA GeForce RTX 4070 Ti với 12 GB video
bộ nhớ: cân bằng tốt về tốc độ, kích thước ngữ cảnh và chỗ cho các mô hình lớn hơn.

Các thẻ từ khoảng RTX 3060 đến RTX 5090 đều có thể hoạt động tốt; sự phù hợp tốt nhất phụ thuộc
về RAM, CPU, làm mát và tệp mô hình bạn cài đặt. Sử dụng cài đặt trước GPU trong
Thanh bên của Evi để phù hợp với phần cứng của bạn.

Chỉ chạy trên CPU (cài đặt trước "CPU … GB RAM") là một phương án dự phòng khẩn cấp:
Evi vẫn có thể sử dụng được mà không cần card đồ họa phù hợp nhưng phản hồi chậm hơn nhiều.
Ưu tiên GPU thực bất cứ khi nào bạn có thể.

--------------------------------------------------------------------------------
  Hoàn toàn di động — khi bạn cần Internet
--------------------------------------------------------------------------------

Evi được xây dựng để có thể di động: sao chép toàn bộ thư mục sang ổ đĩa khác, thẻ nhớ USB,
hoặc PC, sau đó khởi động nó ở đó. Cuộc trò chuyện, kỷ niệm, cài đặt, dữ liệu bảo mật và
tập tin kích hoạt thường nằm trong thư mục đó (kích hoạt được gắn với
PC, không phải đường dẫn thư mục).

Internet chủ yếu dành cho những thứ bạn chọn tải xuống (tệp mẫu, tùy chọn
giọng nói hoặc tính năng bổ sung, cập nhật) và các tính năng tùy chọn như tìm kiếm trên web, thư,
phát trực tuyến hoặc thời tiết khi bạn cho phép truy cập mạng.

Trò chuyện cốt lõi, bộ nhớ, ghi chú, bộ hẹn giờ, công cụ tệp bên trong thư mục được phép của bạn, cục bộ
nhận dạng giọng nói, đầu ra giọng nói cục bộ và khóa quyền riêng tư chạy trên thiết bị của bạn
máy mà không gửi cuộc trò chuyện của bạn tới dịch vụ đám mây. Tùy chọn trực tuyến
các tính năng chỉ chạy khi quyền truy cập mạng được bật và bạn sử dụng chúng.

--------------------------------------------------------------------------------
  Bảo mật: Mở khóa bằng mã PIN và giọng nói (chống sao chép)
--------------------------------------------------------------------------------

Evi có thể sử dụng mã PIN bảo mật và đăng ký giọng nói tùy chọn trên thiết bị của bạn.

Khi sử dụng tính năng mở khóa bằng giọng nói, mỗi lần thử có thể yêu cầu một nhóm từ ngẫu nhiên ngắn
điều đó thay đổi mọi lúc - không phải một cụm từ cố định mãi mãi. Điều đó cản trở sự dễ dàng
thủ thuật phát lại một bản ghi âm cũ của giọng nói của bạn. Mã PIN của bạn vẫn là một
tuyến phòng thủ riêng biệt.

Điều này được thiết kế để ngăn chặn hành vi lạm dụng thông thường; không sản phẩm tiêu dùng nào có thể hứa hẹn
sự hoàn hảo trước mọi cuộc tấn công (ví dụ ai đó có cả mã PIN của bạn và
bắt chước giọng nói phức tạp). Giữ mã PIN của bạn ở chế độ riêng tư và thiết lập đầy đủ như
ứng dụng hướng dẫn bạn.

--------------------------------------------------------------------------------
  Khắc phục sự cố (danh sách kiểm tra ngắn)
--------------------------------------------------------------------------------

• Không có câu trả lời AI/lỗi mô hình
  → Ít nhất một .gguf phù hợp trong models\llm\ ? Xem mô hình\llm\README.txt.
  → Hãy thử model nhỏ hơn hoặc cài đặt trước CPU trong thanh bên nếu đường dẫn GPU không thành công.

• Không có micrô
  → Cài đặt âm thanh Windows: kiểm tra mic. Trong Evi, chọn thiết bị bên dưới
    Micrô và lưu.

• Không có đầu ra giọng nói
  → Kiểm tra xem tập tin giọng nói cho ngôn ngữ của bạn có tồn tại trong thư mục piper\ không và
    chọn một giọng nói trong thanh bên.

• Web hoặc YouTube bị lỗi
  → Tắt "Chặn tất cả lưu lượng truy cập" ở thanh bên nếu bạn muốn các tính năng trực tuyến.
  → Để phát lại YouTube, thường cần có VLC Portable và truy cập mạng.

• Sau khi chỉnh sửa cheat sheet
  → Khởi động lại Evi để tất cả những người trợ giúp văn bản nhận được các thay đổi một cách đáng tin cậy.

--------------------------------------------------------------------------------
  Khắc phục sự cố (tham khảo mở rộng)
--------------------------------------------------------------------------------

Kiểm tra nhanh (luôn luôn đầu tiên)
  • Windows 10 hay 11 64-bit, được cập nhật, khởi động lại sau những thay đổi lớn?
  • Evi chạy từ một thư mục được giải nén hoàn toàn — không phải từ bên trong kho lưu trữ?
  • Tránh các thư mục được đồng bộ hóa trên đám mây (OneDrive, v.v.) cho thư mục dữ liệu trực tiếp trong khi
    Evi chạy — sử dụng đường dẫn cục bộ như C:\EviPortable hoặc D:\Tools\Evi khi
    có thể.
  • Dung lượng đĩa trống có đủ cho mô hình, cuộc trò chuyện và cập nhật không?
  • Sau khi thay đổi model, giọng nói hoặc cheat sheet: thoát hoàn toàn Evi và bắt đầu
    một lần nữa.

1) Hệ điều hành
  • Evi chỉ dành cho Windows 10 và 11; các phiên bản hệ điều hành khác không được hỗ trợ.
  • Nếu ứng dụng hoàn toàn không khởi động, hãy giải nén toàn bộ gói, kiểm tra phần mềm chống vi-rút
    log cho các tệp thực thi bị chặn và thử đường dẫn cài đặt ngắn hơn mà không gặp phải trường hợp hiếm gặp nào.
    Các ký tự chỉ có Unicode.

2) Đường dẫn thư mục, phần mềm chống virus, tính di động
  • Thêm một loại trừ cho thư mục gốc Evi của bạn trong phần mềm bảo mật nếu quá trình quét thực hiện
    khởi động rất chậm hoặc khóa tập tin trong quá trình tải xuống.
  • USB: thích USB 3 + NTFS; phương tiện truyền thông rất chậm làm cho các mô hình lớn trở nên đau đớn.

3) Mô hình ngôn ngữ (.gguf)
  • Triệu chứng: không trả lời, lỗi mô hình, không tải được ngay lập tức.
  • sửa lỗi: xác minh models\llm\ chứa một .gguf hoàn chỉnh (không phải 0 byte); tải lại
nếu cần thiết; khớp kích thước mô hình với VRAM bằng cách sử dụng models\llm\README.txt; nếu không chắc chắn,
    giữ một tệp q4_k_m đã được kiểm tra trong thư mục.
  • nhiều tệp .gguf: Evi có thể chọn tệp lớn nhất phù hợp với VRAM của bạn — nếu bạn
    nghi ngờ có xung đột, hãy kiểm tra chỉ với một tệp.

4) GPU, CUDA, trình điều khiển, hết bộ nhớ
  • Cập nhật trình điều khiển NVIDIA; trên laptop buộc GPU/hiệu năng rời
    chế độ dành cho Evi nơi Windows cho phép.
  • Nếu bạn thấy OOM hoặc GPU gặp sự cố, hãy sử dụng điểm kiểm tra nhỏ hơn, đóng các ứng dụng GPU khác,
    nhiệt độ thấp hơn hoặc chuyển sang cài đặt sẵn của CPU (chậm hơn nhưng ổn định hơn).

5) Chế độ chỉ dành cho CPU
  • Dự kiến sẽ chậm; RAM hệ thống đủ trống; đóng các tác vụ nền nặng;
    sử dụng gói năng lượng "Hiệu suất cao" trong thời gian dài.

6) Kích hoạt
  • Dán các phím cẩn thận (không có dấu cách thừa); các khóa được gắn với một ID máy.
  • Sau những thay đổi lớn về phần cứng, bạn có thể cần một khóa thay thế — hãy sử dụng dịch vụ hỗ trợ
    địa chỉ với các chi tiết của bạn.

7) Micrô
  • Quyền riêng tư của Windows → Micrô → cho phép các ứng dụng trên máy tính để bàn.
  • Đặt đúng thiết bị ghi mặc định; trong Evi chọn cùng một thiết bị và Lưu.
  • Tai nghe Bluetooth có thể tăng thêm độ trễ — hãy kiểm tra bằng micrô USB nếu không chắc chắn.
  • Ứng dụng khác có thể giữ chế độ độc quyền — tạm thời đóng phần mềm cuộc họp.

8) Nhận dạng giọng nói (cục bộ)
  • Nếu quá trình nhận dạng không bao giờ kết thúc, hãy đảm bảo các tệp mô hình trong models\whisper được
    nguyên vẹn và cho phép mạng tìm nạp mô hình lần đầu nếu bản dựng của bạn cần.

9) Đầu ra giọng nói (Piper / TTS)
  • Xác nhận piper\ chứa gói giọng nói cho ngôn ngữ giao diện người dùng của bạn; chọn một giọng nói trong
    thanh bên; kiểm tra bộ trộn âm lượng Windows - Evi có thể bị tắt tiếng trên mỗi ứng dụng.

10) Mạng và "Chặn tất cả lưu lượng truy cập"
  • Tắt tính năng chặn đối với web, người trợ giúp thư, thời tiết hoặc nội dung tải xuống.
  • Proxy hoặc VPN của công ty có thể yêu cầu trợ giúp về CNTT cho danh sách cho phép.

11) YouTube và phương tiện truyền thông
  • Giữ nguyên bố cục VLC Portable đi kèm; cho phép truy cập mạng; đọc
    Hướng dẫn Portable\VLCPortable nếu đường dẫn đã được di chuyển.

12) Ngôn ngữ giao diện người dùng và bảng ghi chú
  • Bảng cheat được cung cấp cho mỗi tệp ngôn ngữ trong cheatsheets\ — xem cheatsheets\README.txt.
  • Lưu các chỉnh sửa dưới dạng UTF-8; khởi động lại Evi sau khi chỉnh sửa.

13) Bảo mật (mã PIN / mở khóa bằng giọng nói)
  • Sử dụng môi trường yên tĩnh; kiểm tra lại mức tăng micrô; không bao giờ chia sẻ mã PIN của bạn.
  • Lời nhắc từ ngẫu nhiên là có chủ ý — không nên mở khóa các bản ghi âm giọng nói cũ.

14) Hiệu suất, treo máy, treo máy
  • Giảm kích thước mô hình, cải thiện khả năng làm mát, đọc mọi sự cố.log trong cây nếu
    build tạo một cái và khôi phục thay đổi cuối cùng bạn đã thực hiện trước khi thất bại.

15) Khi liên hệ với bộ phận hỗ trợ
  • Bao gồm Machine ID, phiên bản Windows, model GPU + VRAM + driver, trong đó .gguf
    bạn sử dụng và văn bản lỗi chính xác (không phải khóa bí mật).

Tài liệu tham khảo khắc phục sự cố đầy đủ (ngôn ngữ này): Manual\FEHLERSUCHE_VI.txt

--------------------------------------------------------------------------------
  Hỗ trợ - khóa nối tiếp và ID máy
--------------------------------------------------------------------------------

Email: Brielbeck@hotmail.de
Luôn bao gồm ID máy của bạn từ màn hình kích hoạt khi yêu cầu
khóa nối tiếp hoặc khóa thay thế sau khi thay đổi phần cứng.

=======================================================================================