"""
Response utility for standardized API responses.
"""
class Response:
    """
    Utility class for formatting success and error responses.
    """
    @staticmethod
    def success(message, data=None):
        """Return a success response dictionary."""
        return{
            "success": True,
            "message": message,
            "data": data
        }
    
    @staticmethod
    def error(message, error_type="system"):
        """Return an error response dictionary."""
        return{
            "success": False,
            "message": message,
            "type": error_type
        }