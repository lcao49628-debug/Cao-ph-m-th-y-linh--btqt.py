import json

students = []


def get_avg_score(student):
    return student['avg_score']

def get_name(student):

    return student['name'].split()[-1]

def get_valid_score(subject_name):
    """Bẫy lỗi: Ép người dùng phải nhập điểm từ 0 đến 10 và không được nhập chữ"""
    while True:
        try:
            score = float(input(f"Nhập điểm môn {subject_name} (0-10): "))
            if 0 <= score <= 10:
                return score
            else:
                print("Lỗi: Điểm phải nằm trong khoảng từ 0 đến 10. Vui lòng nhập lại!")
        except ValueError:
            print("Lỗi: Bạn vừa nhập chữ hoặc ký tự lạ. Vui lòng nhập một con số!")




# HIỂN THỊ DANH SÁCH 
def display_students():
    print("\n--- DANH SÁCH SINH VIÊN HIỆN TẠI ---")
    if len(students) == 0:
        print("Danh sách hiện đang trống!")
        return
        

    print("-" * 80)
    print(f"| {'Mã SV':<7} | {'Họ và Tên':<20} | {'Toán':<5} | {'Lý':<5} | {'Hóa':<5} | {'ĐTB':<5} | {'Xếp loại':<10} |")
    print("-" * 80)
    

    for student in students:
        print(f"| {student['id']:<7} | {student['name']:<20} | {student['math']:<5.1f} | {student['physics']:<5.1f} | {student['chemistry']:<5.1f} | {student['avg_score']:<5.2f} | {student['grade']:<10} |")
    print("-" * 80)


#  THÊM MỚI SINH VIÊN 
def add_student():
    print("\n--- THÊM MỚI SINH VIÊN ---")
    student_id = input("Nhập Mã SV mới: ").strip().upper()
    

    for student in students:
        if student['id'] == student_id:
            print("Lỗi: Mã sinh viên này đã tồn tại trên hệ thống!")
            return 
            
    name = input("Nhập Họ và Tên sinh viên: ").strip()
    

    math_score = get_valid_score("Toán")
    physics_score = get_valid_score("Lý")
    chemistry_score = get_valid_score("Hóa")
        
    avg_score = round((math_score + physics_score + chemistry_score) / 3, 2)
    
    if avg_score < 5.0: grade = "Yếu"
    elif avg_score < 7.0: grade = "TB"
    elif avg_score < 8.0: grade = "Khá"
    else: grade = "Giỏi"
        
    new_student = {
        "id": student_id,
        "name": name,
        "math": math_score,
        "physics": physics_score,
        "chemistry": chemistry_score,
        "avg_score": avg_score,
        "grade": grade
    }
    
    students.append(new_student)
    print("Thành công: Đã tiếp nhận thêm sinh viên mới!")


#  CẬP NHẬT THÔNG TIN 
def update_student():
    print("\n--- CẬP NHẬT THÔNG TIN SINH VIÊN ---")
    search_id = input("Nhập Mã SV cần điều chỉnh điểm: ").strip().upper()
    
    for student in students:
        if student['id'] == search_id:
            print(f"Hệ thống tìm thấy sinh viên: {student['name']}")
            
            new_math = get_valid_score("Toán mới")
            new_physics = get_valid_score("Lý mới")
            new_chemistry = get_valid_score("Hóa mới")
                
            student['math'] = new_math
            student['physics'] = new_physics
            student['chemistry'] = new_chemistry
            student['avg_score'] = round((new_math + new_physics + new_chemistry) / 3, 2)
            
            if student['avg_score'] < 5.0: student['grade'] = "Yếu"
            elif student['avg_score'] < 7.0: student['grade'] = "TB"
            elif student['avg_score'] < 8.0: student['grade'] = "Khá"
            else: student['grade'] = "Giỏi"
            
            print("Thành công: Kết quả học tập của sinh viên đã được cập nhật!")
            return
            
    print("Lỗi: Không tìm thấy sinh viên nào có mã vừa nhập.")


#  XÓA SINH VIÊN 
def delete_student():
    print("\n--- XÓA SINH VIÊN KHỎI HỆ THỐNG ---")
    search_id = input("Nhập Mã SV muốn xóa: ").strip().upper()
    
    for i in range(len(students)):
        if students[i]['id'] == search_id:
            confirm = input(f"Bạn có CHẮC CHẮN muốn xóa '{students[i]['name']}'? (Y/N): ").strip().upper()
            if confirm == "Y":
                del students[i]
                print("Thành công: Dữ liệu sinh viên đã được xóa bỏ hoàn toàn!")
            else:
                print("Hệ thống: Đã hủy thao tác xóa.")
            return
            
    print("Lỗi: Mã sinh viên không tồn tại.")


# TÌM KIẾM SINH VIÊN 
def search_student():
    print("\n--- TÌM KIẾM SINH VIÊN ---")
    keyword = input("Nhập Mã SV hoặc Tên cần tìm kiếm: ").strip().lower()
    found = False
    
    for student in students:
        if keyword == student['id'].lower() or keyword in student['name'].lower():
            print("=> Kết quả:", student['id'], "-", student['name'], "| ĐTB:", student['avg_score'], "| Xếp loại:", student['grade'])
            found = True
            
    if not found:
        print("Không tìm thấy kết quả nào phù hợp.")


#  SẮP XẾP DANH SÁCH 
def sort_students():
    print("\n--- SẮP XẾP DANH SÁCH SINH VIÊN ---")
    print("1. Sắp xếp theo Điểm TB giảm dần")
    print("2. Sắp xếp theo Tên tăng dần từ A đến Z")
    choice = input("Vui lòng nhập lựa chọn (1-2): ").strip()
    
    if choice == "1":
        students.sort(key=get_avg_score, reverse=True)
        print("Đã sắp xếp theo Điểm TB giảm dần! Chọn chức năng 1 để xem bảng.")
    elif choice == "2":
        students.sort(key=get_name)
        print("Đã sắp xếp theo Tên (A-Z)! Chọn chức năng 1 để xem bảng.")
    else:
        print("Lỗi: Lựa chọn tính năng sắp xếp không hợp lệ!")


# THỐNG KÊ ĐIỂM TB
def statistics():
    print("\n--- THỐNG KÊ ĐIỂM SỐ HỌC LỰC ---")
    excellent = 0
    good = 0
    average = 0
    weak = 0
    
    for student in students:
        if student['grade'] == "Giỏi": excellent += 1
        elif student['grade'] == "Khá": good += 1
        elif student['grade'] == "TB": average += 1
        elif student['grade'] == "Yếu": weak += 1
        
    print(f"- Sinh viên loại Giỏi: {excellent}")
    print(f"- Sinh viên loại Khá: {good}")
    print(f"- Sinh viên loại Trung Bình: {average}")
    print(f"- Sinh viên loại Yếu: {weak}")


# LIỆT KÊ ĐIỂM CAO NHẤT / THẤP NHẤT 
def find_min_max():
    print("\n--- SINH VIÊN CÓ ĐIỂM TB CAO NHẤT VÀ THẤP NHẤT ---")
    if len(students) == 0:
        print("Danh sách đang trống!")
        return
        
    max_avg = students[0]['avg_score']
    min_avg = students[0]['avg_score']
    
    for student in students:
        if student['avg_score'] > max_avg: max_avg = student['avg_score']
        if student['avg_score'] < min_avg: min_avg = student['avg_score']
        
    print(f"\n[+] Điểm trung bình CAO NHẤT: {max_avg}")
    for student in students:
        if student['avg_score'] == max_avg:
            print("  - Danh tính:", student['name'])
            
    print(f"\n[-] Điểm trung bình THẤP NHẤT: {min_avg}")
    for student in students:
        if student['avg_score'] == min_avg:
            print("  - Danh tính:", student['name'])


#  PHÂN LOẠI HỌC LỰC 
def classify_students():
    print("\n--- DANH SÁCH CHI TIẾT THEO PHÂN LOẠI HỌC LỰC ---")
    excellent_group = []
    good_group = []
    average_group = []
    weak_group = []
    
    for student in students:
        if student['grade'] == "Giỏi": excellent_group.append(student)
        elif student['grade'] == "Khá": good_group.append(student)
        elif student['grade'] == "TB": average_group.append(student)
        elif student['grade'] == "Yếu": weak_group.append(student)
        
    print("\n[+] PHÂN NHÓM SINH VIÊN GIỎI:")
    if len(excellent_group) == 0: print("  (Không có sinh viên)")
    for student in excellent_group: print("  ->", student['name'], f"- ĐTB: {student['avg_score']}")
        
    print("\n[+] PHÂN NHÓM SINH VIÊN KHÁ:")
    if len(good_group) == 0: print("  (Không có sinh viên)")
    for student in good_group: print("  ->", student['name'], f"- ĐTB: {student['avg_score']}")
        
    print("\n[+] PHÂN NHÓM SINH VIÊN TRUNG BÌNH:")
    if len(average_group) == 0: print("  (Không có sinh viên)")
    for student in average_group: print("  ->", student['name'], f"- ĐTB: {student['avg_score']}")
        
    print("\n[+] PHÂN NHÓM SINH VIÊN YẾU:")
    if len(weak_group) == 0: print("  (Không có sinh viên)")
    for student in weak_group: print("  ->", student['name'], f"- ĐTB: {student['avg_score']}")


# THOÁT VÀ LƯU DỮ LIỆU 
def save_and_exit():
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(students, file, indent=4, ensure_ascii=False)
    print("\nĐã lưu toàn bộ dữ liệu vào file data.json thành công!")



def main():
    global students
    
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            students = json.load(file)
    except FileNotFoundError:
        students = [] 
        
    while True:
        print("\n" + "="*50)
        print("     HỆ THỐNG MENU QUẢN LÝ SINH VIÊN (PTIT-CLI)")
        print("="*50)
        print("1. Hiển thị danh sách sinh viên")
        print("2. Tiếp nhận thêm sinh viên mới")
        print("3. Cập nhật thông tin kết quả học tập")
        print("4. Xóa sinh viên khỏi danh sách")
        print("5. Tìm kiếm sinh viên")
        print("6. Sắp xếp danh sách sinh viên")
        print("7. Thống kê điểm trung bình")
        print("8. Liệt kê sinh viên có điểm TB Cao nhất / Thấp nhất")
        print("9. Phân loại danh sách học lực sinh viên")
        print("10. Lưu lại dữ liệu và Thoát")
        print("="*50)
        
        choice = input("Mời bạn chọn một tính năng (1-10): ").strip()
        
        match choice:
            case "1": display_students()
            case "2": add_student()
            case "3": update_student()
            case "4": delete_student()
            case "5": search_student()
            case "6": sort_students()
            case "7": statistics()
            case "8": find_min_max()
            case "9": classify_students()
            case "10":
                save_and_exit()
                print("Chương trình kết thúc. Tạm biệt!")
                break
            case _:
                print("Lỗi: Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 10!")


if __name__ == "__main__":
    main()