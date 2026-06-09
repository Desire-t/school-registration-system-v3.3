from repository.admin_repository.admin_repository import AdminRepository
from services.admin_services.admin_service import AdminService

def create_admin_service():
    repo = AdminRepository()
    repo.create_admin_table()
    return AdminService()

def test_save_admin():
    service = create_admin_service()
    result = service.save_admin("Engr", "0124", "tambe")
    assert result['success'] is True


def test_update_admin():
    repo = AdminRepository()
    repo.create_admin_table()
    repo.save_admin("Mr tataw", "0121", "Eze")
    service = create_admin_service()
    result = service.update_admin("Mr tataw", "Eze", "0121")
    assert result['success'] is True

def test_fetch_all_admins():
    repo = AdminRepository()
    repo.create_admin_table()
    repo.save_admin("Engineer eze", "0122", "tambe")
    service = create_admin_service()
    result = service.fetch_all_admins()
    assert result['success'] is True
    assert isinstance(result['data'], list)

def test_fetch_admin_by_batch_id():
    repo = AdminRepository()
    repo.create_admin_table()
    repo.save_admin("Engineer eze", "0123", "tambe")
    service = create_admin_service()
    result = service.fetch_admin_by_batch_id("0123")
    assert result['success'] is True
    assert result['data']['batch_id'] == "0123"


