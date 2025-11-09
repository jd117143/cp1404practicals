"""
CP1404 - Practical 7
Project Management program.
Estimate: 1 hour, 30 minutes
Actual:
(Time details for Project class module + project management combined)
"""

import datetime
from prac_07.project import Project

FILENAME = "projects.txt"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""


def main():
    """Run the Project Management program."""
    print("Welcome to Project Manager")
    projects = load_projects()

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_projects(filename=FILENAME):
    """Load projects from file."""
    projects = []
    with open(filename) as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])

            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
        print(f"Loaded {len(projects)} from {filename}")
    return projects


def save_projects(projects, filename=FILENAME):
    """Save projects to file."""
    with open(filename, "w") as out_file:
        for project in projects:
            start_date_string = project.start_date.strftime("%d/%m/%Y")
            print(f"{project.name}\t{start_date_string}\t{project.priority}\t{project.cost_estimate:.2f}\t"
                  f"{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display projects, sorted by priority."""
    incomplete_projects = sorted([project for project in projects if not project.is_complete()])
    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")

    completed_projects = sorted([project for project in projects if project.is_complete()])
    print("Completed projects: ")
    for project in completed_projects:
        print(f"  {project}")


if __name__ == '__main__':
    main()
