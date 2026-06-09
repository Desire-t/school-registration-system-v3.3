
import bcrypt
from repository.admin_repository.admin_repository import AdminRepository
from services.admin_services.auth_service import AdminAuthService

def test_authentication():
    repo = AdminRepository()
    repo.create_admin_table()
    password = "tambe"
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    repo.save_admin("Auth Admin", "0131", hashed_password)

    auth_service = AdminAuthService()
    result = auth_service.authenticate_admin("0131", password)
    assert result['success'] is True

