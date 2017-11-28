
class Teacher(object):
    def __init__(self,teacherName):
        self.teacherName = teacherName
        self.teachClass = {}

    def teacherAddClass(self,classname,classObj):

        self.teachClass[classname] = classObj

