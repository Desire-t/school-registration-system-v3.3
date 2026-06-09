"""
Repository for student data access and manipulation.
"""
import sqlite3
from utils.response import Response

from utils.base_repository import BaseRepository
from datetime import datetime

class StudentRepository(BaseRepository):
    """
    Handles CRUD operations for student records in the database.
    """
    def create_students_table(self):
        """Create the students table in the database."""
        response = Response()
        try:
            with self.get_connection() as conn:
                conn.execute("""
                            CREATE TABLE IF NOT EXISTS students(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                age INTEGER NOT NULL,
                                matricule TEXT UNIQUE NOT NULL,
                                department TEXT NOT NULL,
                                english FLOAT NOT NULL,
                                french FLOAT NOT NULL,
                                total_marks FLOAT NOT NULL,
                                average FLOAT NOT NULL,
                                grade TEXT NOT NULL,
                                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                            )
                            """)
            return response.success("Student table initialized")
        except sqlite3.Error as e:
            return response.error("Failed to initialize student table", error_type="system")
    
    def save_student(self, name, age, matricule, department, english, french, total_marks, average, grade):
        """Save a new student record to the database."""
        response = Response()
        try:
            with self.get_connection() as conn:
                conn.execute("""
                            INSERT INTO students(
                                name,
                                age,
                                matricule,
                                department,
                                english,
                                french,
                                total_marks,
                                average,
                                grade
                            )
                            VALUES(?,?,?,?,?,?,?,?,?)
                            """,(name,
                                age,
                                matricule,
                                department,
                                english,
                                french,
                                total_marks,
                                average,
                                grade
                            ))
            return response.success("Student record created")
        except sqlite3.IntegrityError as e:
            return response.error("Student with this matricule already exists", error_type="duplicate")
        except sqlite3.Error as e:
            return response.error("Failed to create student", error_type="system")
    
    def fetch_student_by_matricule(self, matricule):
        """Fetch a student by matricule."""
        response = Response()
        try:
            with self.get_connection() as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM students WHERE matricule=?", (matricule,))
                row = cursor.fetchone()
            result = dict(row) if row else None
            if result:
                return response.success("Student retrieved",result)
            else:
                return response.error("Student not found", error_type="not_found")
        except sqlite3.Error as e:
            return response.error("Failed to retrieve student", error_type="system")
    
    def fetch_all_students(self):
        """Fetch all students from the database."""
        response = Response()
        try:
            with self.get_connection() as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM students")
                rows = cursor.fetchall()
            result = [dict(row) for row in rows]
            if result:
                return response.success("Students retrieved", result)
            else:
                return response.error("No students found", error_type="not_found")
        except sqlite3.Error as e:
            return response.error("Failed to retrieve students", error_type="system")
    
    def fetch_student_by_name(self, name):
        """Fetch a student by name."""
        response = Response()
        try:
            with self.get_connection() as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM students WHERE name=?", (name,))
                row = cursor.fetchone()
            result = dict(row) if row else None
            if result:
                return response.success("Student retrieved", result)
            else:
                return response.error("Student not found", error_type="not_found")
        except sqlite3.Error as e:
            return response.error("Failed to retrieve student", error_type="system")
    
    def update_student(self, name, age, department, english, french, total_marks, average, grade, matricule, timestamp): 
        """Update an existing student record in the database."""
        response = Response()
        try:
            with self.get_connection() as conn:
                conn.execute("""
                            UPDATE students
                            SET name=?,
                            age=?,
                            department=?,
                            english=?,
                            french=?,
                            total_marks=?, 
                            average=?,
                            grade=?,
                            updated_at=? WHERE matricule=?""",
                            (name, age, department, english, french, total_marks, average, grade, timestamp, matricule))
            return response.success("Student details updated")
        except sqlite3.IntegrityError as e:
            return response.error("Student with this matricule already exists", error_type="duplicate")
        except sqlite3.Error as e:
            return response.error("Failed to update student", error_type="system")
