"""
Base repository utility for database connection management.
"""
import sqlite3

class BaseRepository:
    """
    Base class for repository classes to manage database connections.
    """
    def __init__(self, db_path="school.db"):
        """Initialize with database path."""
        self._db_path = db_path
    
    def get_connection(self):
        """Get a new database connection."""
        return sqlite3.connect(self._db_path)
