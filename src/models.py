from dataclasses import dataclass, field
from typing import Dict, List, Optional

GRADE_POINTS: Dict[str, float] = {
    "A": 10.0,
    "A-": 9.0,
    "B": 8.0,
    "B-": 7.0,
    "C": 6.0,
    "C-": 5.0,
    "D": 4.0,
    "E": 2.0,
    "F": 0.0,
    "F*": 0.0,
}


@dataclass
class Course:
    code: str
    name: str
    credits: float
    grade: str

    def grade_point(self) -> Optional[float]:
        return GRADE_POINTS.get(self.grade)


@dataclass
class Semester:
    number: int
    year: int
    type: str
    courses: List["Course"] = field(default_factory=list)

    def total_credits(self) -> float:
        return sum(c.credits for c in self.courses if c.grade in GRADE_POINTS)

    def total_weighted_points(self) -> float:
        return sum(
            c.credits * c.grade_point() for c in self.courses if c.grade in GRADE_POINTS
        )

    def sgpa(self) -> Optional[float]:
        total_credits = self.total_credits()
        if total_credits == 0:
            return None
        return round(self.total_weighted_points() / total_credits, 2)


@dataclass
class Transcript:
    semesters: List[Semester] = field(default_factory=list)

    def total_credits(self) -> float:
        return sum(sem.total_credits() for sem in self.semesters)

    def total_weighted_points(self) -> float:
        return sum(sem.total_weighted_points() for sem in self.semesters)

    def cgpa(self) -> Optional[float]:
        total_credits = self.total_credits()
        if total_credits == 0:
            return None
        return round(self.total_weighted_points() / total_credits, 2)

    def rolling_cgpa(self, semester_number: int) -> Optional[float]:
        if semester_number > len(self.semesters) or semester_number <= 0:
            raise ValueError(f"Invalid semester number: {semester_number}")

        selected_semesters = self.semesters[:semester_number]

        total_credits = sum(sem.total_credits() for sem in selected_semesters)
        if total_credits == 0:
            return None

        total_weighted_points = sum(
            sem.total_weighted_points() for sem in selected_semesters
        )
        return round(total_weighted_points / total_credits, 2)
