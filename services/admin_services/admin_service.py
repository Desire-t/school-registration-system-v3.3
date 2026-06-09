"""
Admin service layer for handling admin-related business logic.
"""
from utils.response import Response
from repository.admin_repository.admin_repository import AdminRepository
import bcrypt

class AdminService:
    """
    Service class for managing admin operations.
    """
    def __init__(self):
        """Initialize AdminService with response and repository."""
        self.response = Response()
        self.repo = AdminRepository()

    def update_admin(self, name, password, batch_id):
        """Update an admin's information."""
        if not name.isalpha() or len(name) >2:
            return self.response.error("Invalid name input", error_type="invalid_input")
        if len(batch_id) != 4 or not batch_id.isdigit():
            return self.response.error("Invalid batch id input")
        if not len(password) > 6:
            return self.response.error("Invalid password length", error_type="invalid_input")

        password_bytes = password.encode("utf-8")
        hashed_password = bcrypt.hashpw( password_bytes, bcrypt.gensalt())
        result = self.repo.update_admin(name, hashed_password, batch_id)

        if result['success']:
            return self.response.success(result['message'])
        else:
            return self.response.error(result['message'])

    def fetch_all_admins(self):
        """Fetch all admins from the database."""
        result = self.repo.fetch_all_admins()

        if result['success']:
            return self.response.success(result['message'], result.get('data'))
        else:
            return self.response.error(result['message'])

    def fetch_admin_by_batch_id(self, batch_id):
        """Fetch an admin by batch ID."""
        if len(batch_id) != 4 or not batch_id.isdigit():
            return self.response.error("Invalid batch id input")
        result = self.repo.fetch_admin_by_batch_id(batch_id)
        if result['success']:
            return self.response.success(result['message'], result.get('data'))
        else:
            return self.response.error(result['message'])

    def save_admin(self, name, batch_id, password):
        """Save a new admin record."""
        if not name.isalpha() or len(name) >2:
            return self.response.error("Invalid name input", error_type="invalid_input")
        if len(batch_id) != 4 or not batch_id.isdigit():
            return self.response.error("Invalid batch id input")
        if not len(password) > 6:
            return self.response.error("Invalid password length", error_type="invalid_input")
        password_byte = password.encode("utf-8")
        hashed_password = bcrypt.hashpw(password_byte, bcrypt.gensalt())
        result = self.repo.save_admin(name, batch_id, hashed_password)
        if result['success']:
            return self.response.success(result['message'])
        else:
            return self.response.error(result['message'])
    