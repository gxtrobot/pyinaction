'''
分数处理程序最终版
文本格式如下

学号,姓名,语文,数学,英语
1,王小明,100,88,90
2,李思思,90,70,85
3,刘畅,88,78,92

'''

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

    def add_score(self, score):
        value = int(score)
        if value < 0:
            raise ValueError('{} must above 0'.format(value))
        if value > 100:
            raise ValueError('{} must less than 100'.format(value))
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
        print('总人数:', count)
        print('平均分:', avg)
        print('最高分:', highest, students[idx][1])

    def __str__(self):
        return '课程: {}'.format(self.name)


if __name__ == "__main__":
    f_name = 'scores_final.txt'
    myclass = ClassRoom('五一班')
    # 读取第一行
    f = open(f_name, encoding='utf-8')
    title_line = f.readline()
    lines = f.readlines()
    f.close()

    # process first line
    title_line = title_line.strip()
    titles = title_line.split(',')
    lessons_title = titles[2:]
    lessons = []
    for title in lessons_title:
        lesson = Lesson(title)
        myclass.add_lesson(lesson)
        lessons.append(lesson)

    for line in lines:
        line = line.strip()
        items = line.split(',')
        scores = items[2:]
        myclass.add_student(items[0], items[1])
        for i in range(len(lessons)):
            lessons[i].add_score(scores[i])
    myclass.print_details()