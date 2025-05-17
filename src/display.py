from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from models import Semester, Transcript


class Display:
    def __init__(self, transcript: Transcript):
        self.transcript = transcript
        self.console = Console()

    def show_semester_details(self, semester: Semester) -> None:
        courses_table = Table(
            title=f"Semester {semester.number} ({semester.type} {semester.year}) Courses"
        )
        courses_table.add_column("Code", style="cyan")
        courses_table.add_column("Name", style="magenta")
        courses_table.add_column("Credits", style="green")
        courses_table.add_column("Grade", style="yellow")
        courses_table.add_column("Grade Points", style="blue")

        for course in semester.courses:
            grade_point = course.grade_point() or "N/A"
            courses_table.add_row(
                course.code,
                course.name,
                str(course.credits),
                course.grade,
                str(grade_point),
            )

        summary_panel = Panel(
            f"Total Credits: [green]{semester.total_credits()}[/]\n"
            f"Total Weighted Points: [blue]{semester.total_weighted_points()}[/]\n"
            f"SGPA: [bold yellow]{semester.sgpa() or 'N/A'}[/]",
            title=f"Semester {semester.number} Summary",
        )

        self.console.print(summary_panel)
        self.console.print(courses_table)

    def show_cgpa_breakdown(self) -> None:
        overall_panel = Panel(
            f"Total Credits: [green]{self.transcript.total_credits()}[/]\n"
            f"Total Weighted Points: [blue]{self.transcript.total_weighted_points()}[/]\n"
            f"CGPA: [bold yellow]{self.transcript.cgpa() or 'N/A'}[/]",
            title="Overall Academic Summary",
        )

        semesters_table = Table(title="Semester-wise Performance")
        semesters_table.add_column("Semester", style="cyan")
        semesters_table.add_column("Type/Year", style="magenta")
        semesters_table.add_column("Credits", style="green")
        semesters_table.add_column("SGPA", style="yellow")
        semesters_table.add_column("Cumulative Credits", style="blue")
        semesters_table.add_column("Rolling CGPA", style="bold yellow")

        cumulative_credits = 0
        cumulative_points = 0

        for semester in self.transcript.semesters:
            sem_credits = semester.total_credits()
            sem_points = semester.total_weighted_points()

            cumulative_credits += sem_credits
            cumulative_points += sem_points

            rolling_cgpa = (
                round(cumulative_points / cumulative_credits, 2)
                if cumulative_credits > 0
                else None
            )

            semesters_table.add_row(
                str(semester.number),
                f"{semester.type} {semester.year}",
                str(sem_credits),
                str(semester.sgpa() or "N/A"),
                str(cumulative_credits),
                str(rolling_cgpa or "N/A"),
            )

        self.console.print(overall_panel)
        self.console.print(semesters_table)

    def show_menu(self) -> None:
        while True:
            self.console.clear()
            self.console.print(
                Panel(
                    "[bold]Transcript Analysis System[/]\n"
                    "1. Semester-wise Breakdown\n"
                    "2. CGPA Breakdown\n",
                    title="Main Menu",
                    border_style="blue",
                )
            )

            choice = input("Select an option (or 'q' to quit): ").strip().lower()

            if choice == "q":
                break
            elif choice == "1":
                self._show_semester_menu()
            elif choice == "2":
                self.console.clear()
                self.show_cgpa_breakdown()
                input("\nPress Enter to return to main menu...")

    def _show_semester_menu(self) -> None:
        while True:
            self.console.clear()
            self.console.print(
                Panel(
                    "[bold]Select a semester to view details:[/]",
                    title="Semester-wise Breakdown",
                    border_style="green",
                )
            )

            for i, semester in enumerate(self.transcript.semesters, 1):
                self.console.print(
                    f"{i}. Semester {semester.number} ({semester.type} {semester.year})",
                    style="cyan",
                )

            self.console.print("\nPress Enter to return to main menu", style="yellow")

            choice = input("\nSelect a semester: ").strip()

            if not choice:
                break

            if choice.isdigit():
                choice_num = int(choice)
                if 1 <= choice_num <= len(self.transcript.semesters):
                    self.console.clear()
                    self.show_semester_details(
                        self.transcript.semesters[choice_num - 1]
                    )
                    input("\nPress Enter to return...")
