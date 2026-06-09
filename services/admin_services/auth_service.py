"""
Authentication service for admin login and validation.
"""
from repository.admin_repository.admin_repository import AdminRepository
from utils.response import Response
import bcrypt

class AdminAuthService():
    """
    Service class for authenticating admin users.
    """
    def __init__(self):
        """Initialize AdminAuthService with repository and response."""
        self._repo = AdminRepository()
        self.response = Response()

    def authenticate_admin(self, batch_id, password):
        """Authenticate an admin using batch ID and password."""
        print(f"[DEBUG] Received batch_id: '{batch_id}' password: '{password}'")
        if len(batch_id) != 4 or not batch_id.isdigit():
            print("[DEBUG] Invalid batch id input format")
            return self.response.error("Invalid batch id input")
        result = self._repo.fetch_admin_by_batch_id(batch_id)
        if not result['success']:
            print("[DEBUG] Admin not found for batch_id")
            return self.response.error("Invalid batch ID")

        admin = result['data']
        stored_password = admin['password']
        print(f"[DEBUG] Stored hash from DB: {stored_password}")
        password_bytes = password.encode("utf-8")
        if bcrypt.checkpw(password_bytes, stored_password):
            print("[DEBUG] Password match: SUCCESS")
            return self.response.success("Login successful", admin)
        else:
            print("[DEBUG] Password match: FAIL")
            return self.response.error("Incorrect password")
