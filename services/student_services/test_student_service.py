from services.student_services.student_service import StudentService

def create_student_service():
    service = StudentService()
    service.create_students_table()
    return service

def test_create_students_table():
    service = create_student_service()
    result = service.create_students_table()
    assert result['success'] is True

def test_fetch_all_students():
    service = create_student_service()
    service.save_student("Mr eze", 12, "ICT001", "Dept", 12, 10)
    result = service.fetch_all_students()
    assert result['success'] is True
    assert isinstance(result['data'], list)

def test_save_student():
    service = create_student_service()
    result = service.save_student("Mr eze", 12, "ICT002", "Dept", 12, 10)
    assert result['success'] is True

def test_fetch_student_by_matricule():
    service = create_student_service()
    service.save_student("Mr eze", 12, "ICT003", "Dept", 12, 10)
    result = service.fetch_student_by_matricule("ICT003")
    assert result['success'] is True
    assert result['data']['matricule'] == "ICT003"

def test_fetch_student_by_name():
    service = create_student_service()
    service.save_student("Mr eze", 12, "ICT004", "Dept", 12, 10)
    result = service.fetch_student_by_name("Mr eze")
    assert result['success'] is True
    assert result['data']['name'] == "Mr eze"

def test_update_student():
    service = create_student_service()
    service.save_student("Engr T-boy", 12, "ICT005", "Dept", 12, 10)
    result = service.update_student("Engr T-boy", 12, "Dept", 12, 10, "ICT005")
    assert result['success'] is True
