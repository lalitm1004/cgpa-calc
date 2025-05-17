import tomllib
from typing import Any, Dict, List
from pathlib import Path

from models import Course, Semester, Transcript


def read_toml_file(path: Path = Path("./grades.toml")) -> Dict[str, Any]:
    with open(path, "rb") as f:
        data = tomllib.load(f)
    return data


def parse_courses_by_semester(data: Dict[str, Any]) -> Transcript:
    semesters: List[Semester] = []

    for sem_key, sem_data in data.items():
        if not sem_key.startswith("sem"):
            continue

        sem_number = int(sem_key[3:])
        year = sem_data.get("year", 0)
        type = sem_data.get("type", "Unknown")

        course_dict = sem_data.get("course", {})
        course_list: List[Course] = []

        for course_code, course_info in course_dict.items():
            course = Course(
                code=course_code,
                name=course_info.get("name", ""),
                credits=course_info.get("credits", 0.0),
                grade=course_info.get("grade", ""),
            )
            course_list.append(course)

        semester = Semester(
            number=sem_number, year=year, type=type, courses=course_list
        )
        semesters.append(semester)

    return Transcript(semesters)
