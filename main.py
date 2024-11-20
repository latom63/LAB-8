#--- Перша частина завдання Гетьмана Ярослава ----

# Словник для зберігання інформації про студентів
students_dict = {
    "group_number": 102,  # Номер групи
    "students": [
        {
            "name": "Сидоренко Марія Іванівна",  # ПІБ студента
            "course": 1,  # Курс
            "subjects": {  # Оцінки за предметами
                "Математика": 80,
                "Інформатика": 90,
                "Фізика": 85
            }
        },
        {
            "name": "Кравченко Олег Сергійович",
            "course": 1,
            "subjects": {
                "Математика": 70,
                "Інформатика": 85,
                "Фізика": 75
            }
        }
    ]
}

# Функція для додавання нового студента
def add_student(students_dict, name, course, subjects):
    """
    Додає інформацію про нового студента до словника.
    :param students_dict: Словник із студентами.
    :param name: ПІБ студента.
    :param course: Курс студента.
    :param subjects: Предмети та оцінки.
    """
    new_student = {
        "name": name,
        "course": course,
        "subjects": subjects
    }
    students_dict["students"].append(new_student)

# Виклик функції для додавання нового студента
add_student(
    students_dict,
    "Іванов Андрій Михайлович",
    1,
    {
        "Математика": 85,
        "Інформатика": 88,
        "Фізика": 80
    }
)

# --------- Друга частина завдання --- Микитенка Мирослава ----

# Оцінка структури словника:
# Словник загалом є структурованим і дозволяє зручно зберігати дані. 
# Немає необхідності змінювати структуру, оскільки всі необхідні дані присутні.

# Функція для обчислення середньої оцінки студента
def calculate_average(subjects):
    """
    Обчислює середню оцінку за всіма предметами.
    :param subjects: Словник із предметами та оцінками.
    :return: Середня оцінка.
    """
    return sum(subjects.values()) / len(subjects)

# Функція для сортування студентів за середньою оцінкою
def sort_students_by_average(students_dict):
    """
    Сортує студентів за середньою оцінкою у порядку спадання.
    :param students_dict: Словник із студентами.
    """
    students_dict["students"].sort(
        key=lambda student: calculate_average(student["subjects"]),
        reverse=True
    )

# Виклик функції сортування
sort_students_by_average(students_dict)

# Виведення результатів після сортування
print("Список студентів після сортування за середньою оцінкою:")
for student in students_dict["students"]:
    avg = calculate_average(student["subjects"])
    print(f"{student['name']} - Середня оцінка: {avg:.2f}")
