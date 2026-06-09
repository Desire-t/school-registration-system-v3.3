"""
Calculation utility for grading and marks computation.
"""
class Calculation:
    """
    Utility class for calculating marks and grades.
    """
    GRADE_THRESHOLDS = [
        (14, "A+"),
        (13, "A"),
        (12.5, "B+"),
        (12, "B"),
        (11.5, "C+"),
        (10, "C"),
    ]

    @staticmethod
    def calculate_marks(english: float, french: float) -> tuple[float, float]:
        """Calculate total marks and weighted average."""
        total_marks = english + french
        weighted_average = ((english * 4) + (french * 4)) / 8
        return total_marks, weighted_average

    @classmethod
    def grade(cls, average: float) -> str:
        """Return grade letter based on average."""
        for threshold, letter in cls.GRADE_THRESHOLDS:
            if average >= threshold:
                return letter
        return "D"

