"""
Student service layer for handling student-related business logic.
"""
from repository.student_repository.student_repository import StudentRepository
from utils.response import Response
from utils.calculation import Calculation
from datetime import datetime

class StudentService:
    """
    Service class for managing student operations.
    """
    def __init__(self):
        """Initialize StudentService with repository, response, and calculator."""
        self._repo = StudentRepository()
        self.response = Response()
        self._calculator = Calculation()

    def create_students_table(self):
        """Create the students table in the database."""
        result = self._repo.create_students_table()
        if result['success']:
            return self.response.success(result['message'])
        else:
            return self.response.error(result['message'], error_type="system")

    def fetch_all_students(self):
        """Fetch all students from the database."""
        result = self._repo.fetch_all_students()
        if result['success']:
            return self.response.success(result['message'], result.get('data'))
        else:
            return self.response.error(result['message'])

    def fetch_student_by_matricule(self, matricule):
        """Fetch a student by matricule."""
        result = self._repo.fetch_student_by_matricule(matricule)
        if result['success']:
            return self.response.success(result['message'], result.get('data'))
        else:
            return self.response.error(result['message'])

    def fetch_student_by_name(self, name):
        """Fetch a student by name."""
        result = self._repo.fetch_student_by_name(name)
        if result['success']:
            return self.response.success(result['message'], result.get('data'))
        else:
            return self.response.error(result['message'])

    def save_student(self, name, age, matricule, department, english, french):
        """Save a new student record."""
        total_marks, average = self._calculator.calculate_marks(english, french)
        grade = self._calculator.grade(average)
        result = self._repo.save_student(name, age, matricule, department, english, french, total_marks, average, grade)
        if result['success']:
            return self.response.success(result['message'])
        else:
            return self.response.error(result['message'], error_type=result.get('type', 'system'))

    def update_student(self, name, age, department, english, french, matricule):
        """Update an existing student record."""
        total_marks, average = self._calculator.calculate_marks(english, french)
        grade = self._calculator.grade(average)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = self._repo.update_student(name, age, department, english, french, total_marks, average, grade, matricule, timestamp)
        if result['success']:
            return self.response.success(result['message'])
        else:
            return self.response.error(result['message'], error_type=result.get('type', 'system'))