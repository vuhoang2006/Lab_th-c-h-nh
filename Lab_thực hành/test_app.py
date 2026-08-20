import unittest
import os
import sqlite3
from app import init_db, add_student, delete_student

class TestStudentApp(unittest.TestCase):
    def setUp(self):
        init_db()

    def test_add_and_delete(self):
        add_student("SV01", "Nguyen Van A", 20, 3.5)
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id='SV01'")
        student = cursor.fetchone()
        self.assertIsNotNone(student)
        self.assertEqual(student[1], "Nguyen Van A")
        conn.close()

        delete_student("SV01")
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id='SV01'")
        student = cursor.fetchone()
        self.assertIsNone(student)
        conn.close()

if __name__ == '__main__':
    unittest.main()