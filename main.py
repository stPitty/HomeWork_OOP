class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []

    def __str__(self):
        result = f"""Имя: {self.name} 
Фамилия: {self.surname}"""
        return result


students_list = []
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses = []
        self.grades = {}
        students_list.append(self)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses and course in lecturer.courses:
            if grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Оценки только по 10-ти бальной шкале'
        else:
            return 'Ошибка'

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def grade_average(self):
        counter = 0
        res = 0
        for course in self.courses:
            if course in self.grades:
                res += sum(self.grades[course])/len(self.grades[course])
                counter += 1
        res = round(res/counter,2)
        return res

    def __str__(self):
        result = f"""{Mentor.__str__(self)}
Средняя оценка за домашние задания: {self.grade_average()}
Курсы в процессе изучения: {", ".join(self.courses)}
Завершенные курсы: {", ".join(self.finished_courses)}"""
        return result
    def __lt__(self, other):
        if not isinstance(other,Student):
            return 'Вы сравниваете не студентов'
        else:
            return self.grade_average() < other.grade_average()

lecturer_list = []
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}
        lecturer_list.append(self)

    def __lt__(self, other):
        if not isinstance(other,Lecturer):
            return 'Вы сравниваете не лекторов'
        else:
            return self.grade_average() < other.grade_average()

    def grade_average(self):
        return Student.grade_average(self)


    def __str__(self):
        result = f"""{super().__str__()}
Средняя оценка за лекции: {self.grade_average()} """
        return result


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses and course in student.courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# ---------------------------------------------Объявляем представителей класса
Petr = Student ('Peter', 'Stankin', 'Male')
Petr.courses = ['Python', 'Mini']
Petr.grades['Python'] = [7,5,3,4]

Vasya = Student ('Vasya', 'Pupkin', 'Male')
Vasya.courses = ['Python']
Vasya.grades['Python'] = [1,7,4,9]

Lena = Student ('Lena', 'Grecha', 'Female')
Lena.courses = ['Geo']
Lena.grades['Geo'] = [5,1,3,5]

Levov = Reviewer('Igor','Levov')
Levov.courses = ['Python']

Stanley = Reviewer('James','Stanley')
Stanley.courses = ['Python']

Harrison = Lecturer('Alex','Harrison')
Harrison.courses = ['Python']
Harrison.grades['Python'] = [4,8,2,5]

Martin = Lecturer('Martin','Ebby')
Martin.courses = ['Python']
Martin.grades['Python'] = [5,1,3,6]

# --------------------------------------------Работаем с представителями
Petr.rate_lec(Harrison,'Python',6)
Petr.add_courses('Math')

Vasya.rate_lec(Martin,'Python',2)
Vasya.add_courses('Biology')

Levov.rate_hw(Petr,'Python',5)
Stanley.rate_hw(Vasya,'Python',4)

def people_avg_grades(people_list,course):
    avg = 0
    counter = 0
    for people in people_list:
        if course in people.courses and course in people.grades:
            avg += sum(people.grades[course])/len(people.grades[course])
            counter += 1
    if counter == 0:
        return 'Ошибка'
    else:
        avg = round(avg/counter,2)
        return avg

# ---------------------------------------------------------Выводим результаты
print('Сравнения:')
print(Petr > Vasya)
print(Petr < Harrison)
print(Martin < Vasya)
print(Harrison > Martin, end='\n\n')
print('Принтуем объекты:')
print(Petr, Vasya, Lena, Levov, Stanley, Harrison, Martin, sep='\n\n', end='\n\n')
print('Принтуем средние оценки:')
print(f"Средняя оценка за лекции преподователей по курсу Python: {people_avg_grades(lecturer_list,'Python')}")
print(f"Средняя оценка за домашние задания по курсу Python: {people_avg_grades(students_list,'Python')}")