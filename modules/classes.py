
class Class(object):
    def __init__(self,className,classCourse):
        self.className = className
        self.classCourse = classCourse
        self.classStudent = {}

    def addStudent(self,studentName,studentObj):
        self.classStudent[studentName] = studentObj