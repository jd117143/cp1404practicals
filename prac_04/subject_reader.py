"""
CP1404 - Practical 4
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Get subject data from file and display it."""
    subjects = load_data(FILENAME)
    display_subjects(subjects)


def load_data(filename=FILENAME):
    """Load data from file formatted as: subject, lecturer, number of students."""
    subjects = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subjects.append(parts)
    input_file.close()
    return subjects


def display_subjects(subjects):
    """Display subjects, lecturers, and student numbers in aligned columns."""
    max_subject_len = max(len(subject[0]) for subject in subjects)
    max_teacher_len = max(len(subject[1]) for subject in subjects)
    max_students_len = max(len(str(subject[2])) for subject in subjects)

    for subject in subjects:
        print(f"{subject[0]:{max_subject_len}} is taught by "
              f"{subject[1]:{max_teacher_len}} and has "
              f"{subject[2]:{max_students_len}} students")


main()
