from modules.classes import Class
from modules.major import Course
from modules.student import Student
from modules.teacher import Teacher


class School(object):
    def __init__(self,schoolName):
        self.schoolName = schoolName
        self.schoolCourse = {}
        self.schoolClass = {}
        self.schoolTeacher = {}
        self.schoolStudent = {}


    # 创建课程
    def createCourse(self,courseName,courseTime,coursePrice):
        courseObj = Course(courseName,courseTime,coursePrice)
        self.schoolCourse[courseName] = courseObj


    # 创建班级
    def createClass(self,className,courseObj):
        classObj = Class(className,courseObj)
        self.schoolClass[className] = classObj

    # 创建老师
    def createTeacher(self,teacherName,teachClass):
        teacherObj = Teacher(teacherName)
        teacherObj.teacherAddClass(teachClass.className,teachClass)   #给老师分班级
        self.schoolTeacher[teacherName] = teacherObj



    # 学生注册
    def createStudent(self,studentName,className):
        studentObj = Student(studentName)
        classObj = self.schoolClass[className]
        self.schoolStudent[studentName] = studentObj    # 学校学生字典里加新学生
        classObj.addStudent(studentName,studentObj)     # 班级类中加学生
        self.schoolClass[className] = classObj      # 更新学校的班级字典


    # 显示课程
    def showCourse(self):
        for course in self.schoolCourse:
            course = self.schoolCourse[course]
            print("课名：%s 课时：%s 价格：%s" %(course.courseName,course.courseTime,course.coursePrice))

    # 显示班级
    def showClass(self):
        for oneClass in self.schoolClass:
            oneClass = self.schoolClass[oneClass]
            stuList = []
            for stu in oneClass.classStudent:
                stuList.append(oneClass.classStudent[stu].studentName)
            print("班级:",oneClass.className," 课程:",oneClass.classCourse.courseName," 学生:",stuList)

    # 显示老师
    def showTeacher(self):
        for teacher in self.schoolTeacher:
            teacher = self.schoolTeacher[teacher]
            cla = []
            for classes in teacher.teachClass:
                cla.append(teacher.teachClass[classes].className)
            print("姓名：%s 所教班级：%s" %(teacher.teacherName,cla))
