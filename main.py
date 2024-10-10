# Створення словника з інформацією про студентів
students = {
    1: {
        'group_number': 'CS-21',
        'name': 'Іванов Іван Іванович',
        'course': 2,
        'subjects': {
            'Математика': 85,
            'Фізика': 90,
            'Програмування': 95
        }
    },
    2: {
        'group_number': 'CS-21',
        'name': 'Петров Петро Петрович',
        'course': 2,
        'subjects': {
            'Математика': 75,
            'Фізика': 80,
            'Програмування': 85
        }
    }
}

# Функція для додавання нового студента до словника
def add_student(student_id, group_number, name, course, subjects):
    students[student_id] = {
        'group_number': group_number,
        'name': name,
        'course': course,
        'subjects': subjects
    }

# Приклад додавання нового студента
add_student(3, 'CS-21', 'Сидоров Сидір Сидорович', 2, {'Математика': 88, 'Фізика': 92, 'Програмування': 90})

# Функція для обчислення середнього балу студента
def calculate_average_grade(subjects):
    return sum(subjects.values()) / len(subjects)

# Функція для сортування студентів за середнім балом
def sort_students_by_average():
    sorted_students = sorted(students.items(), key=lambda x: calculate_average_grade(x[1]['subjects']), reverse=True)
    return sorted_students

# Виведення відсортованого списку студентів за середнім балом
def print_sorted_students():
    sorted_students = sort_students_by_average()
    for student_id, info in sorted_students:
        print(f"ID студента: {student_id}")
        print(f"Група: {info['group_number']}, Ім'я: {info['name']}, Курс: {info['course']}")
        print(f"Середній бал: {calculate_average_grade(info['subjects']):.2f}")
        print("Предмети та оцінки:")
        for subject, grade in info['subjects'].items():
            print(f" - {subject}: {grade}")
        print()

# Виклик функції для виведення відсортованого списку студентів
print("Відсортований список студентів за середнім балом:")
print_sorted_students()
