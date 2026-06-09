"""
Repository for admin data access and manipulation.
"""
import sqlite3
from utils.response import Response
from utils.base_repository import BaseRepository
from datetime import datetime

class AdminRepository(BaseRepository):
    """
    Handles CRUD operations for admin records in the database.
    """
    def create_admin_table(self):
        """Create the admins table in the database."""
        response = Response()
        
        try:
            with self.get_connection() as conn:
                conn.execute("""
                            CREATE TABLE IF NOT EXISTS admins(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                batch_id TEXT UNIQUE NOT NULL,
                                password  BLOB NOT NULL,
                                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                            )
                            """)
            return response.success("Admin table initialized")
        except sqlite3.Error as e:
            return response.error("Failed to initialize admin table", error_type="system")
    
    def save_admin(self, name, batch_id, password):
        """Save a new admin record to the database."""
        response = Response()
        try:
            with self.get_connection() as conn:
                conn.execute("""
                            INSERT INTO admins(
                                name,
                                batch_id,
                                password
                            )
                            VALUES(?,?,?)
                            """, (name, batch_id, password))
            return response.success("Admin created")
        except sqlite3.IntegrityError as e:
            return response.error("Admin with this batch ID already exists", error_type="duplicate")
        except sqlite3.Error as e:
            return response.error("Failed to create admin", error_type="system")
    
    def fetch_admin_by_batch_id(self, batch_id):
        """Fetch an admin by batch ID."""
        response = Response()
        try:
            with self.get_connection() as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM admins WHERE batch_id=?", (batch_id,))
                row = cursor.fetchone()

                result = dict(row) if row else None
            if result:
                return response.success("Admin retrieved",result)
            else:
                return response.error("Admin not found", error_type="not_found")
        except sqlite3.Error as e:
            return response.error("Failed to retrieve admin", error_type="system")
    
    def fetch_all_admins(self):
        """Fetch all admins from the database."""
        response = Response()
        try:
            with self.get_connection() as conn:
                conn.row_factory = sqlite3.Row
                
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM admins")
                rows = cursor.fetchall()
            result = [dict(row) for row in rows]
            return response.success("Admins retrieved",result)
        except sqlite3.Error as e:
            return response.error("Failed to retrieve admins", error_type="system")
    def update_admin(self, name, password, batch_id):
        """Update an admin's information in the database."""
        response = Response()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with self.get_connection() as conn:
                cursor = conn.execute("""
                            UPDATE admins SET name=?, password=?, updated_at=? WHERE batch_id=?
                            """,(name, password, timestamp, batch_id))

            return response.success("Admin updated")
        except sqlite3.IntegrityError as e:
            return response.error("Admin with this batch ID already exists", error_type="duplicate")
        except sqlite3.Error as e:
            return response.error("Failed to update admin", error_type="system")
