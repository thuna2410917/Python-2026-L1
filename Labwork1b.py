while True:
    print("\n--- MENU QUẢN LÝ ---")
    print("1. Nhập sinh viên")
    print("2. Nhập khóa học")
    print("3. Nhập điểm")
    print("4. Xem danh sách khóa học")
    print("5. Xem danh sách sinh viên")
    print("6. Xem điểm khóa học")
    print("0. Thoát")
    
    chon = input("Nhập lựa chọn của bạn (0-6): ")


    if chon == "1":
        so_sv = int(input("Nhập số lượng sinh viên: "))
        for i in range(so_sv):
            print(f"Nhập thông tin sinh viên thứ {i+1}:")
            sv_id = input("  ID sinh viên: ")
            sv_ten = input("  Tên sinh viên: ")
            sv_dob = input("  Ngày sinh: ")
            
            sv = {"id": sv_id, "name": sv_ten, "dob": sv_dob}
            students.append(sv)
        print("-> Đã thêm sinh viên xong!")


    elif chon == "2":
        so_kh = int(input("Nhập số lượng khóa học: "))
        for i in range(so_kh):
            print(f"Nhập thông tin khóa học thứ {i+1}:")
            kh_id = input("  ID khóa học: ")
            kh_ten = input("  Tên khóa học: ")
            
            kh = {"id": kh_id, "name": kh_ten}
            courses.append(kh)
        print("-> Đã thêm khóa học xong!")


    elif chon == "3":
        if len(courses) == 0:
            print("Chưa có khóa học nào! Hãy nhập khóa học trước.")
        elif len(students) == 0:
            print("Chưa có sinh viên nào! Hãy nhập sinh viên trước.")
        else:
            kh_id = input("Nhập ID khóa học cần nhập điểm: ")
            
            
            if kh_id not in marks:
                marks[kh_id] = {}
            
            
            for sv in students:
                diem = float(input(f"Nhập điểm cho {sv['name']} (ID: {sv['id']}): "))
                marks[kh_id][sv["id"]] = diem
            print("-> Nhập điểm thành công!")

    elif chon == "4":
        print("\n--- DANH SÁCH KHÓA HỌC ---")
        if len(courses) == 0:
            print("Chưa có khóa học nào.")
        else:
            for kh in courses:
                print("ID:", kh["id"], "| Tên:", kh["name"])


    elif chon == "5":
        print("\n--- DANH SÁCH SINH VIÊN ---")
        if len(students) == 0:
            print("Chưa có sinh viên nào.")
        else:
            for sv in students:
                print("ID:", sv["id"], "| Tên:", sv["name"], "| Ngày sinh:", sv["dob"])


    elif chon == "6":
        kh_id = input("Nhập ID khóa học muốn xem điểm: ")
        if kh_id in marks:
            print(f"\n--- BẢNG ĐIỂM KHÓA HỌC {kh_id} ---")
            for sv in students:
                s_id = sv["id"]
                # Lấy điểm ra, nếu chưa có thì hiện "Chưa có điểm"
                if s_id in marks[kh_id]:
                    print("Tên:", sv["name"], "| Điểm:", marks[kh_id][s_id])
                else:
                    print("Tên:", sv["name"], "| Điểm: Chưa có")
        else:
            print("Khóa học này chưa được nhập điểm!")

    elif chon == "0":
        print("Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ, hãy chọn lại!")