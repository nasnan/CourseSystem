import sys
import os

BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf.settings import *
from conf.common import *
from database.dbapi import *
from modules.school import School


class start(object):


    def welcome(self):

        choose_dict ={
            "1": schoolManage,
            "2":teacherManage,
            "3":studentManage,
            "q":exit
        }


        while 1:
            print("请选择：\n1.学校视图\n2.教师视图\n3.学生视图\nq.退出")
            choose = checkInput(choose_dict)
            choose_dict[choose]()







# 学校视图
class schoolManage(object):
    def __init__(self):
        self.school_db = load_data_from_db(database_dir)    #将本地数据读到self.school_db
        self.welcome()


    def welcome(self):

        choose_dict = {
            "1":self.createClass,
            "2":self.createCourse,
            "3":self.createTeacher,
            "4":self.showClass,
            "5":self.showCourse,
            "6":self.showTeacher,
            "q":exit
        }


        while 1 :
            print("请选择:\n1.创建班级\n2.创建课程\n3.创建老师\n4.显示班级\n5.显示课程\n6.显示老师\nq.退出")
            choose = checkInput(choose_dict)
            choose_dict[choose]()
            wait()


    def saveChange(self):
        write_new_to_db(database_dir, self.school_db)


    def createClass(self):
        className = input("请输入班级号：")
        if checkRepeat(className,self.school_db.schoolClass,"班级") == 0:
            return 0

        courseList = self.school_db.schoolCourse
        self.showCourse()
        print("请输入该班级关联的课程：")
        classCourse = checkInput(courseList)
        courseObj = self.school_db.schoolCourse[classCourse]
        self.school_db.createClass(className,courseObj)
        print("创建成功！")
        self.saveChange()




    def createCourse(self):
        courseName = input("请输入课程名字：")

        if checkRepeat(courseName,self.school_db.schoolCourse,"课程") == 0:
            return 0
        courseTime = input("请输入课程课时：")
        coursePrice = input("请输入课程价格：")
        self.school_db.createCourse(courseName,courseTime,coursePrice)
        print("创建成功！")
        self.saveChange()


    # 创建老师
    def createTeacher(self):
        teacherName = input("请输入老师姓名：")
        if checkRepeat(teacherName,self.school_db.schoolTeacher,"老师") == 0:
            return 0
        busyClass = set()
        for tea in self.school_db.schoolTeacher:
            for cla in self.school_db.schoolTeacher[tea].teachClass:
                busyClass.add(cla)
        while 1:
            print("请输入任课班级")
            self.showClass()
            classNumber = checkInput(self.school_db.schoolClass)
            if classNumber not in busyClass:
                break
            else:
                print("此班级已有任课老师！")
        classObj = self.school_db.schoolClass[classNumber]
        self.school_db.createTeacher(teacherName,classObj)
        print("创建成功！")
        self.saveChange()



    def showClass(self):
        self.school_db.showClass()

    def showCourse(self):
        self.school_db.showCourse()


    def showTeacher(self):
        self.school_db.showTeacher()






# 老师视图
class teacherManage(object):

    def __init__(self):
        school_db = load_data_from_db(database_dir)
        self.teacher_db = school_db.schoolTeacher
        self.welcome()


    def welcome(self):
        print("请输入老师姓名:")
        teacherName = checkInput(self.teacher_db)
        self.teacherObj = self.teacher_db[teacherName]
        self.class_list = self.teacherObj.teachClass
        print("wlecome!")

        while 1:
            choose_dic = {
                "1":self.showClass,
                "2":self.showStudent,
                "q":exit
            }

            print("请选择：\n1.查看所教班级\n2.查看班级学生\nq.退出")
            choose = checkInput(choose_dic)
            choose_dic[choose]()
            wait()



    def showClass(self):
        print("所教班级有：")
        for cla in self.class_list:
            print(self.class_list[cla].className)


    def showStudent(self):
        print("选择要查看的班级：")
        className = checkInput(self.class_list)
        classObj = self.class_list[className]
        print("%s 课程：%s 学生列表：%s" %(classObj.className,classObj.classCourse.courseName,classObj.classStudent))



# 学生视图
class studentManage(object):

    def __init__(self):
        self.school_db = load_data_from_db(database_dir)
        self.student_list = self.school_db.schoolStudent
        self.welcome()


    def welcome(self):
        while 1:
            print("请选择：\n1.注册\n2.登陆\nq.退出")
            choose_dict = {
                "1":self.signUp,
                "q":exit
            }

            choose = checkInput(choose_dict)
            choose_dict[choose]()


    # 注册
    def signUp(self):

        while 1:
            studentName = input("请输入名字：")
            if studentName not in self.student_list:
                break
            else:
                print("名字已存在！")

        self.school_db.showClass()
        print("请选择班级：")
        className = checkInput(self.school_db.schoolClass)
        courseObj = self.school_db.schoolClass[className].classCourse
        print("此班级的课程%s课时为：%s，价格为%s。" %(courseObj.courseName,courseObj.courseTime,courseObj.coursePrice))
        print("输入y确认，q退出！")
        choose_list = ["q","y"]
        choose = checkInput(choose_list)
        if choose == "y":
            self.school_db.createStudent(studentName,className)
            self.saveChange()
            print("注册成功！")
        else:
            exit()



    def saveChange(self):
        write_new_to_db(database_dir, self.school_db)

