#Mr.Wiggins grade scale


class Student:
#The weight of the grades for each section
    number_of_std = 0
    homework = 30
    project = 30
    quiz = 20
    test = 20
    grade_track = {} #A dictionary that keeps track of students grades

    def __init__(self,first_N,last_N,gender,year=None,id= None,average=0):
        self.first_N = first_N
        self.last_N = last_N
        self.year = year
        self.average = average
        self.homework_avg = 30
        self.project_avg = 30
        self.quiz_avg = 20
        self.test_avg = 20
        self.id = id
        self.gender = gender
        Student.number_of_std+=1
#Calculates the average of each section and add records to the grade tracker
#values should be placed in a list
    def add_grades(self,value,typ):
        average = (sum(value) / len(value)) / 100
        typ = typ.lower()
        if typ == 'homework':
            if typ in self.grade_track.keys():
                self.grade_track[typ].extend(value)
                average = (sum(self.grade_track[typ]) / len(self.grade_track[typ])) / 100
                self.homework_avg = average * self.homework
            else:
                self.homework_avg = average * self.homework
                self.grade_track[typ] = value

        elif typ == 'project':
            if typ in self.grade_track.keys():
                self.grade_track[typ].extend(value)
                average = (sum(self.grade_track[typ]) / len(self.grade_track[typ])) / 100
                self.project_avg = average * self.project

            else:
                self.project_avg = average * self.project
                self.grade_track[typ] = value

        elif typ == 'quiz':
            if typ in self.grade_track.keys():
                self.grade_track[typ].extend(value)
                average = (sum(self.grade_track[typ]) / len(self.grade_track[typ])) / 100
                self.quiz_avg = average * self.quiz

            else:
                self.quiz_avg = average * self.quiz
                self.grade_track[typ] = value

        elif typ == 'test':
            if typ in self.grade_track.keys():
                self.grade_track[typ].extend(value)
                average = (sum(self.grade_track[typ]) / len(self.grade_track[typ])) / 100
                self.test_avg = average * self.test

            else:
                self.test_avg = average * self.test
                self.grade_track[typ] = value

        else:
            print('Invalid Type')



#Calculates the students overall average
    def total_average(self):
        self.average = self.homework_avg + self.project_avg + self.quiz_avg + self.test_avg
        return '{} overall average is {}'.format(self.first_N,self.average)

#Deletes grades from selected section
    def clear_grades(self,section):
        if section == 'homework':
            self.homework_avg = self.homework
        elif section == 'quiz':
            self.quiz_avg = self.quiz
        elif section == 'test':
            self.test_avg == self.test
        elif section == 'project':
            self.project_avg == self.project
        else:
            print('Invalid section')
        del self.grade_track[section]


    def __repr__(self):
        return "Student('{}','{}','{}')".format(self.first_N,self.last_N,self.year)






student1 = Student('javed','wiggins','male','senior',1)
#print(student1.total_average())

student1.add_grades([90,95,90],'Homework')
print(student1.total_average())
#print(student1.number_of_std)
#print(student1.grade_track)
student1.add_grades([50,95,90],'homework')
print(student1.grade_track)
print(student1.total_average())
print(student1.homework_avg)

student1.add_grades([50,45,70],'quiz')
#print(student1.total_average())
#print(student1.clear_grades('h'))
print(student1.grade_track)
print(student1.total_average())
print(student1.clear_grades('homework'))
print(student1.grade_track)
print(student1.total_average())
print(student1.__repr__())
print(student1.gender)
