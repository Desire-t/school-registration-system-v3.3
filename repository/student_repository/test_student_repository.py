from repository.student_repository.student_repository import StudentRepository
from datetime import datetime

def create_student_repo():
    repo = StudentRepository()
    repo.create_students_table()
    return repo

def test_create_students_table():
    repo = create_student_repo()
    result = repo.create_students_table()
    assert result["success"] is True

def test_save_student():
    repo = create_student_repo()
    result = repo.save_student(
        "Engr Eze",
        15,
        "ICTU2026-A",
        "ICT",
        75,
        80,
        155,
        77.5,
        "B",
    )
    assert result["success"] is True

def test_fetch_student_by_matricule():
    repo = create_student_repo()
    repo.save_student(
        "Engr Eze",
        15,
        "ICTU2026-B",
        "ICT",
        75,
        80,
        155,
        77.5,
        "B",
    )
    result = repo.fetch_student_by_matricule("ICTU2026-B")
    assert result['success'] is True
    assert result['data']['matricule'] == "ICTU2026-B"

def test_fetch_all_students():
    repo = create_student_repo()
    repo.save_student(
        "Engr Eze",
        15,
        "ICTU2026-C",
        "ICT",
        75,
        80,
        155,
        77.5,
        "B",
    )
    result = repo.fetch_all_students()
    assert result['success'] is True
    assert isinstance(result['data'], list)

def test_fetch_student_by_name():
    repo = create_student_repo()
    repo.save_student(
        "Engr Eze",
        15,
        "ICTU2026-D",
        "ICT",
        75,
        80,
        155,
        77.5,
        "B",
    )
    result = repo.fetch_student_by_name("Engr Eze")
    assert result['success'] is True
    assert result['data']['name'] == "Engr Eze"

def test_update_student():
    repo = create_student_repo()
    matricule = "ICTU2026-E"
    repo.save_student(
        "Engr Eze",
        15,
        matricule,
        "ICT",
        75,
        80,
        155,
        77.5,
        "B",
        
    )
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = repo.update_student("Engr", 12, "ict", 58, 12, 70, 35, "E", matricule, timestamp)
    assert result['success'] is True