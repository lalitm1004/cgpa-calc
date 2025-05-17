from parser import read_toml_file, parse_courses_by_semester
from display import Display


def main():
    data = read_toml_file()
    transcript = parse_courses_by_semester(data)
    display = Display(transcript)
    display.show_menu()


if __name__ == "__main__":
    main()
