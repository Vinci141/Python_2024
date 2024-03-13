class Student:
    total_marks=100
    def __init__(self, name, roll_num, marks):
        self.studentName = name
        self.roll_number = roll_num
        self.studentMarks = marks

    def result(self):
        if self.studentMarks >= 60:
            return 'Pass'
        else:
            return 'Fail'

    def print_details(self):
        print(f'\nName:{self.studentName}')
        print(f'Roll Num:{self.roll_number}')
        print(f'Marks:{self.studentMarks}')
        print(f'Percentage:{int((self.studentMarks/Student.total_marks)*100)}%')


# print('###   During execution of above code, \'self\' is replaced by object name that we have created. In this case, ''self is replaced with student1   ###')

print('Total Marks:',Student.total_marks)
s1 = Student('vinil', 12345, 98)
s2 = Student('mehta', 12344, 10)
s3 = Student('V', 12345, 30)
s4 = Student('M', 12346, 74)
s1.print_details()
s2.print_details()
s3.print_details()
s4.print_details()
