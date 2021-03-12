class LISTA(object):

    def __init__(self,name):
        self.__name = name
        self.__LIST = [0]
        self.__value = 0


    def name(self):
        return self.__name

    def getvalue(self):
        return self.__value

    def setvalue(self,value):
        self.__value = value

    def getlist(self):
        return self.__LIST

    def getitem(self,item):
        return self.__LIST[item]

    def additem(self,arg0):
        self.__LIST.append(arg0)

    def setitem(self,arg0,arg1):
        self.__LIST[arg0] = arg1
        