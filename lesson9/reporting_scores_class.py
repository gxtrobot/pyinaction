import sys


class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.lessons = []

    def __str__(self):
        return '班级: {}'.format(self.name)

    def add_student(self, no, student_name):
        self.students.append((no, student_name))

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def print_details(self):
        print(self)
        print('学号: 姓名 ')
        for no, student_name in self.students:
            print('{:3}: {:>5}'.format(no, student_name))

        for lesson in self.lessons:
            lesson.summary_scores(self.students)


class Lesson:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_scores(self, scores):
        for v in scores:
            value = int(v)
            if value < 0:
                raise ValueError('{} must above 0'.format(value))
            self.scores.append(value)

    def summary_scores(self, students):
        count = len(self.scores)
        total = 0
        avg = 0
        highest = max(self.scores)
        idx = self.scores.index(highest)
        for value in self.scores:
            total += value
        avg = total / count
        print()
        print(self)
        print('count:', count)
        print('avg:', avg)
        print('highest:', highest, students[idx][1])

    def __str__(self):
        return '课程: {}'.format(self.name)


if __name__ == "__main__":
    f_name = 'scores.txt'
    myclass = ClassRoom('五一班')
    lesson_math = Lesson('数学')
    f = open(f_name, encoding='utf-8')
    scores = []
    lines = f.readlines()
    f.close()
    for line in lines:
        items = line.split(',')
        myclass.add_student(items[0], items[1])
        scores.append(items[2])
    lesson_math.add_scores(scores)
    myclass.add_lesson(lesson_math)
    myclass.print_details()
