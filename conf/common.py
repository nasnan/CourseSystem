def checkInput(list):
    while 1:
        inputItemp = input()
        if inputItemp in list:
            return inputItemp
        else:
            print("输入错误，请重新输入")


# def checkRepeat(content,toCheck,name):
#     if content in toCheck:
#         print("此%s已存在" %name)
#         return 0



def checkRepeat(item,list,name):
    if item in list:
        print("%s已存在，输入y修改现有数据，输入q返回" %name)
        chooseList = ["y", "q"]
        choose = checkInput(chooseList)
        if choose == "y":
            return 1
        elif choose == "q":
            return 0

def wait():
    input("输入任意键返回")
