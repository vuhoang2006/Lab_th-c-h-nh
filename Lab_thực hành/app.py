import sqlite3

def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gpa REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_student(id, name, age, gpa):
    try:
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (id, name, age, gpa))
        conn.commit()
        conn.close()
        print("-> Thêm sinh viên thành công!")
    except sqlite3.IntegrityError:
        print("-> Lỗi: Mã sinh viên đã tồn tại!")

def delete_student(id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (id,))
    if cursor.rowcount > 0:
        print("-> Xóa thành công!")
    else:
        print("-> Không tìm thấy sinh viên!")
    conn.commit()
    conn.close()

def view_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    
    print("\n--- DANH SÁCH SINH VIÊN ---")
    if not rows:
        print("Chưa có dữ liệu.")
        return
    for row in rows:
        print(f"Mã: {row[0]} | Tên: {row[1]} | Tuổi: {row[2]} | GPA: {row[3]}")

def main():
    init_db()
    while True:
        print("\n=== QUẢN LÝ SINH VIÊN ===")
        print("1. Thêm sinh viên")
        print("2. Xóa sinh viên")
        print("3. Xem danh sách")
        print("4. Thoát")
        choice = input("Chọn chức năng (1-4): ")
        
        if choice == '1':
            s_id = input("Nhập mã SV: ")
            name = input("Nhập tên SV: ")
            try:
                age = int(input("Nhập tuổi: "))
                gpa = float(input("Nhập điểm GPA: "))
                add_student(s_id, name, age, gpa)
            except ValueError:
                print("-> Lỗi: Tuổi phải là số nguyên, GPA phải là số thực!")
        elif choice == '2':
            s_id = input("Nhập mã SV cần xóa: ")
            delete_student(s_id)
        elif choice == '3':
            view_students()
        elif choice == '4':
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
    # Done lab code review